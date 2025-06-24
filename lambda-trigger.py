import json
import boto3

def lamb_hanlder(event,context):
   glue_job=boto3.client('glue')
   job_name='spark_load_telemetry'
   response=glue_job.start_job_run(JobName=job_name)
   return {
       'statusCode': 200,
       'body': json.dumps(f'triggered :{response}!')
   }