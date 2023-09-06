# AWS-Firehose-Stream-Processor

This AWS Lambda function is designed to transform data records received as input events from kinesis firehose. It performs custom data transformation by decoding base64-encoded payloads, converting them to JSON format based on a provided schema, and then encoding them back to base64 before returning the transformed records.

## Configuration
Before using the function, ensure that you have properly configured the following parameters in the code:

- `bucket`: The name of the Amazon S3 bucket where the schema file (`gcs_schema.csv`) is stored.
- `object_key`: The key of the schema file within the S3 bucket.
- Ensure that the event source (e.g., AWS Kinesis, AWS Firehose) is set up to trigger this Lambda function.

## Script Overview

### 1. Schema Loading
The script starts by loading the schema file from the specified S3 bucket. This schema file is expected to contain a list of field names, which are used to structure the incoming data.

### 2. Data Transformation
For each record in the event, the script performs the following steps:

- Decodes the base64-encoded payload received in the event.
- Parses the payload by splitting it into individual values based on commas.
- Matches the values with the schema field names to create a JSON object.
- Encodes the JSON object back to base64 format.

### 3. Output
The transformed records are collected into an `output` list, and the Lambda function returns these transformed records to the event source.

## How to Use

1. Ensure that you have set up an event source (e.g., AWS Kinesis, AWS Firehose) to trigger this Lambda function when new data arrives.
2. Configure the S3 bucket and schema file details in the code.
3. Deploy the Lambda function in your AWS environment.
4. When new data arrives at the event source, this Lambda function will automatically transform and return the data in the desired format.

## Note

- This Lambda function assumes that the incoming data is in CSV format, and the provided schema defines the structure of the data.
- Customize the `convert_to_json` function if you have specific data transformation requirements.
- Ensure that the Lambda function has the necessary IAM permissions to read from the specified S3 bucket and execute Lambda functions.

Feel free to reach out if you have any questions or need further assistance.
