import base64
import json 
import pandas as pd
import boto3
import io

client = boto3.client('s3')
bucket = "gamechangepoc"
object_key = "gcs_schema.csv"


print('Loading function')
def convert_to_json(payload,schema):
    values = payload.strip().split(',')
    if len(values) == len(schema):
        item = {}
        for i in range(len(schema)):
            item[schema[i]] = values[i]
    return item
    


    

def lambda_handler(event, context):
    output = []
    obj = client.get_object(Bucket=bucket, Key=object_key)
    body_bytes = obj['Body'].read()
    body_io = io.BytesIO(body_bytes)
    schema_df = pd.read_csv(body_io)
    schema = list(schema_df['schema'])

    for record in event['records']:
        
        payload = record['data']
        payload = base64.b64decode(record['data']).decode('utf-8')
        print("payload is:",payload)
        json_data = convert_to_json(payload,schema)
        print(json_data)
        # 
        # payload = base64.b64decode(record['data']).decode('utf-8')
        # Do custom processing on the payload here
        # output_record = {
        #     'recordId': record['recordId'],
        #     'result': 'Ok',
        #     'data': base64.b64encode(payload.encode('utf-8')).decode('utf-8')
        # }
        # 
        output_record = {
            'recordId': record['recordId'],
            'result': 'Ok',
            'data': base64.b64encode(json.dumps(json_data).encode('utf-8')).decode('utf-8')
        }
        output.append(output_record)
    print('Successfully processed {} records.'.format(len(event['records'])))
    return {
        'records': output
        
    }
