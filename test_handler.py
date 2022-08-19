import pytest
import crhelper
from handler import lambda_handler


class MockContext(object):
    """
    Copied from https://github.com/aws-cloudformation/custom-resource-helper/blob/main/tests/test_resource_helper.py
    """

    function_name = "test-function"
    ms_remaining = 9000

    @staticmethod
    def get_remaining_time_in_millis():
        return MockContext.ms_remaining


@pytest.fixture
def create_event():
    return {
        "RequestType": "Create",
        "StackId": "stack-id/stack-id",
        "RequestId": "request-id",
        "LogicalResourceId": "logical-resource-id",
        "ResponseURL": "https://s3.amazonaws.com/test-bucket/test-object",
        "ResourceProperties": {
            "VpcId": "vpc-11111111111111111",
        },
    }


@pytest.fixture
def mocked_send_response(mocker):

    real_send = crhelper.CfnResource._send

    _send_response = mocker.Mock()

    def mocked_send(self, status=None, reason="", send_response=_send_response):
        real_send(self, status, reason, send_response)

    crhelper.CfnResource._send = mocked_send

    yield _send_response

    crhelper.CfnResource._send = real_send


def get_response_body(mocked_send_response):
    mocked_send_response.assert_called()
    return mocked_send_response.call_args.args[1]


def test_handler_fails_on_no_properties(mocked_send_response, create_event):
    del create_event["ResourceProperties"]

    lambda_handler(create_event, MockContext)

    response_body = get_response_body(mocked_send_response)

    assert response_body["Status"] == "FAILED"
    assert response_body["Reason"] == "VpcId property is missing."
