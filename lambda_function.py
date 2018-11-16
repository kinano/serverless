import json
import helpers.images as image_helpers
import helpers.s3 as s3_helpers
import logging
logging.basicConfig()
logger = logging.getLogger('logger')

def handler(event, context):

    body = {
        "message": "A new S3 object has been uploaded",
        "input": event
    }

    logger.error("Received a new S3 event: {}".format(event))
    # Parse the event and extract the file information
    records = event.get("Records", [])

    for rec in records:
        s3_dict = rec.get("s3")
        bucket = {
            'service': 's3',
            'url': 'https://s3.amazonaws.com',
            'name': s3_dict.get("bucket").get("name"),
            'region': rec.get("awsRegion")
        }
        object_key = s3_dict.get("object").get("key")
        image_helpers.handle_image(
            bucket=bucket,
            object_key=object_key
        )

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
