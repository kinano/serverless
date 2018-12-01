Setup a Lambda function that optimizes images uploaded to an S3 bucket. The Lambda function will also generate thumbnails for every image uploaded to the S3 bucket. 

The Lambda function gets executed automatically when a new file is uploaded to the source bucket.

```
-- Setup some environment variables
FUNC_NAME=ENTER_LAMBDA_FUNCTION_NAME
STATEMENT_ID=ENTER_NUMBER
SOURCE_BUCKET=ENTER_SOURCE_S3_BUCKET_NAME
SOURCE_AWS_ACCOUNT=ENTER_AWS_ACCOUNT_ID

-- Allow S3 to invoke our Lambda function on the source bucket
aws lambda add-permission --function-name $FUNC_NAME --principal s3.amazonaws.com --statement-id $STATEMENT_ID --action "lambda:InvokeFunction" --source-arn arn:aws:s3:::$SOURCE_BUCKET --source-account $SOURCE_AWS_ACCOUNT

-- Verify the policy
aws lambda get-policy --function-name $FUNC_NAME

```

* The following link shows how to install requirements.txt using serverless framework
https://serverless.com/blog/serverless-python-packaging/
```
python3 -m venv ./venv && pip3 install Pillow && pip3 freeze > requirements.txt
```

* You can invoke a Lambda function locally using serverless
```
serverless invoke local --function $FUNC_NAME --path ./sample_data.json
```
