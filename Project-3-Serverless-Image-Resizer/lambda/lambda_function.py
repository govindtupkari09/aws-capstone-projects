import json
import boto3
import os
from PIL import Image

s3 = boto3.client("s3")

OUTPUT_BUCKET = "serverless-image-resizer-output-govind-2026"

SIZES = {
    "thumbnail": (150, 150),
    "medium": (500, 500),
    "large": (1000, 1000)
}


def lambda_handler(event, context):

    print("Received event:")
    print(json.dumps(event))

    # Get uploaded file information from S3 event
    record = event["Records"][0]

    input_bucket = record["s3"]["bucket"]["name"]
    input_key = record["s3"]["object"]["key"]

    print(f"Input bucket: {input_bucket}")
    print(f"Input file: {input_key}")

    # Download image from S3 to Lambda temporary storage
    input_file = "/tmp/input-image"

    s3.download_file(
        input_bucket,
        input_key,
        input_file
    )

    # Open image
    image = Image.open(input_file)

    print(f"Original image size: {image.size}")

    results = []

    # Create different image sizes
    for size_name, dimensions in SIZES.items():

        resized_image = image.copy()

        resized_image.thumbnail(dimensions)

        output_file = f"/tmp/{size_name}.jpg"

        # Convert to RGB for JPEG compatibility
        if resized_image.mode in ("RGBA", "P"):
            resized_image = resized_image.convert("RGB")

        resized_image.save(
            output_file,
            format="JPEG",
            quality=85
        )

        # Output path inside S3
        output_key = f"{size_name}/{os.path.basename(input_key)}"

        # Upload resized image
        s3.upload_file(
            output_file,
            OUTPUT_BUCKET,
            output_key,
            ExtraArgs={
                "ContentType": "image/jpeg"
            }
        )

        print(
            f"Created {size_name}: "
            f"s3://{OUTPUT_BUCKET}/{output_key}"
        )

        results.append(output_key)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Image resized successfully",
            "input": input_key,
            "outputs": results
        })
    }