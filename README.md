# CloudFormation Customer Resource Helper Mock

A minimal example of how to mock the the responses sent by the [Custom Resource Helper](https://github.com/aws-cloudformation/custom-resource-helper) (crhelper).

Inspired by the discussion of local testing techniques in [issue #54](https://github.com/aws-cloudformation/custom-resource-helper/issues/54) of that crhelper's GitHub repo.

This allows the responses from the Lambda function to be tested without any connectivity to real AWS account.

Features:

* Sets up a mock context object copied from the crhelper internal testing code.
* Sets up a sample input event from CloudFormation using a PyTest fixture.
* Mocks the internal _send method to capture the response to CloudFormation
* Provides a test helper function to retrive the response to CloudFormation
* Includes one test that checks the fields of the body of that response

Requirements:

* Python 3.8
* Poetry

Clone the repo and in the directory run `poetry install` to set up the virtual environment.

Then use the following command to test locally the crhelper-enabled Lambda function.

```bash
AWS_ACCESS_ID=X AWS_SECRET_ACCESS_KEY=X AWS_DEFAULT_REGION=X poetry run pytest
```

Sample output:

<pre>
<span style="font-weight:bold;">============================= test session starts ==============================</span>
platform linux -- Python 3.8.10, pytest-7.1.2, pluggy-1.0.0
rootdir: /home/isme/Repos/Personal/github/cloudformation-custom-resource-helper-mock
plugins: mock-3.8.2
collected 1 item

test_handler.py <span style="color:green;">.</span><span style="color:green;">                                                        [100%]</span>

<span style="color:green;">============================== </span><span style="font-weight:bold;color:green;">1 passed</span><span style="color:green;"> in 5.19s</span><span style="color:green;"> ===============================</span>
</pre>
