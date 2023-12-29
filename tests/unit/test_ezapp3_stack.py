import aws_cdk as core
import aws_cdk.assertions as assertions

from ezapp3.ezapp3_stack import Ezapp3Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in ezapp3/ezapp3_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Ezapp3Stack(app, "ezapp3")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
