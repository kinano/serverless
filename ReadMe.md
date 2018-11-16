Setup a Lambda function that optimizes images uploaded to an S3 bucket. The Lambda function gets executed automatically when a new file is uploaded to the source bucket.

```
-- Setup some environment variables
FUNC_NAME=ENTER_LAMBDA_FUNCTION_NAME
STATEMENT_ID=ENTER_NUMBER
SOURCE_BUCKET=ENTER_SOURCE_S3_BUCKET_NAME
SOURCE_AWS_ACCOUNT=ENTER_AWS_ACCOUNT_ID

-- Allow S3 to invoke functions on the source bucket
aws lambda add-permission --function-name $FUNC_NAME --principal s3.amazonaws.com --statement-id $STATEMENT_ID --action "lambda:InvokeFunction" --source-arn arn:aws:s3:::$SOURCE_BUCKET --source-account $SOURCE_AWS_ACCOUNT

-- Verify the policy
aws lambda get-policy --function-name $FUNC_NAME
```

* The following link shows how to install requirements.txt using serverless framework
https://serverless.com/blog/serverless-python-packaging/

* Here is a sample S3 event
```
{
    "Records": [
        {
            "eventVersion": "2.0",
            "eventSource": "aws:s3",
            "awsRegion": "",
            "eventTime": "2018-11-16T01: 38: 02.813Z",
            "eventName": "ObjectCreated:Put",
            "userIdentity": {
                "principalId": ""
            },
            "requestParameters": {
                "sourceIPAddress": ""
            },
            "responseElements": {
                "x-amz-request-id": "",
                "x-amz-id-2": ""
            },
            "s3": {
                "s3SchemaVersion": "1.0",
                "configurationId": "AfterUploadConvertFile",
                "bucket": {
                    "name": "",
                    "ownerIdentity": {
                        "principalId": ""
                    },
                    "arn": "arn:aws:s3: : :"
                },
                "object": {
                    "key": "dsc00041.jpg",
                    "size": 143812,
                    "eTag": "2385b240b1037eb7f8e04d335c4baf05",
                    "sequencer": "005BEE1F7A94C5B8A0"
                }
            }
        }
    ]
}
```