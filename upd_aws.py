import boto3
import os 

bucket_name="mydatalakes3"
s3_prefix='raw/'

local_folder='./telemetry_date'

s3 = boto3.client(
    service_name='s3',
    aws_access_key_id='AWS_KEY_ID',
    aws_secret_access_key='AWS_ACCESS_KEY',
    region_name='us-east-1'
)



for i in os.listdir(local_folder):
    if i.endswith(".json"):
        local_path=os.path.join(local_folder,i)
        s3_key=f"{s3_prefix}{i}"
        try:
            s3.upload_file(local_path,bucket_name,s3_key)
            print(f"uploaded:{i}")
        except Exception as e:
            print(f"failed:{e}")    


