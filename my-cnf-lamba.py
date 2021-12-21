from os.path import dirname
import boto3

script_dir = dirname(__file__)
print(script_dir)

# Setting the CLOUDFORMATION api to be called
my_cnf = boto3.client("cloudformation", region_name = "us-east-1") 

stack = ""

with open(f"{script_dir}/Ec2-with-LaunchTemplate.yaml", "r") as fd:
    stack = fd.read()

print(stack)

params = [
    {
        'ParameterKey': 'VPC',
        'ParameterValue': 'vpc-24688d59'
    }
]

#git update for fun
my_cnf.create_stack(StackName = 'myadarshsonare', TemplateBody=stack, Parameters= params)