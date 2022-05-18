import json
import os
import boto3

#create Glue client
client = boto3.client("glue") 
  
def lambda_handler(event, context):
    try:
        response=client.start_crawler(Name="alicecrawler1")
        print("Alice's lamdba worked.")
        print(json.dumps(response,indent=4))

    except Exception as e:
        print(e)

    

 