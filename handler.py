from crhelper import CfnResource

helper = CfnResource(json_logging=False, log_level="INFO", boto_level="CRITICAL")


def lambda_handler(event, context):
    helper(event, context)


@helper.create
@helper.update
def get_vpc_id(event, _):
    try:
        return event["ResourceProperties"]["VpcId"]
    except KeyError:
        raise ResourceException("VpcId property is missing.")


class ResourceException(Exception):
    pass
