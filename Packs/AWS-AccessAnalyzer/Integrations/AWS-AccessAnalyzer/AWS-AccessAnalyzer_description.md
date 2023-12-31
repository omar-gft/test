Before you can use AWS Access Analyzer, you need to perform several configuration steps in your AWS environment.

### Prerequisites
- Attach an instance profile with the required permissions to the XSOAR server or engine that is running on your AWS environment.
- Instance Profile requires minimum permission: sts:AssumeRole.
- Instance Profile requires permission to assume the roles needed by the AWS integrations.

### Configure AWS Settings
- Create an IAM Role for the Instance Profile.
- Attach a Role to the Instance Profile.
- Configure the Necessary IAM Roles that the AWS Integration Can Assume.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {   
            "Sid": "AccessAnalyzerAdmin",
            "Effect": "Allow",
            "Action": "access-analyzer:*",
            "Resource": "*"
        }
    ]
}
```

For detailed instructions, see the [AWS Integrations - Authentication](https://xsoar.pan.dev/docs/reference/articles/aws-integrations---authentication).

