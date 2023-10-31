''' create new spot ec2 instance module '''
import boto3


ec2 = boto3.resource('ec2', region_name='us-east-1')


# create a new EC2 instance
instances = ec2.create_instances(
    # add your private windows ami
    ImageId='<ami-id>',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='<key-name>',
    Placement={
        #  change the AZ per your EBS AZ
        'AvailabilityZone': 'us-east-1a',
    },
    IamInstanceProfile={
        #  choose Arn or Name, not both
        'Arn': 'arn:aws:iam::<aws-account-id>:instance-profile/azure-hosted-agent',
        # 'Name': 'hosted-agent'
    },

    SecurityGroupIds=[
        '<sg-id>',
    ],
    SubnetId='<subnet-id>',
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'windows-iis-webserver'
                },
                {
                    'Key': 'Function',
                    'Value': 'windows-webserver'
                },
            ]
        },
    ],

    InstanceMarketOptions={
        'MarketType': 'spot',
        'SpotOptions': {
            'MaxPrice': '1.000',
            'SpotInstanceType': 'one-time',
            'InstanceInterruptionBehavior': 'terminate'
        },
    }
)
