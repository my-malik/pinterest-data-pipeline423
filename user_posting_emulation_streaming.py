import requests
import json

record_df = {"ind":1,"first_name":"Mike","last_name":"Cart","age":37,"date_joined":"2024-03-23 13:00:00"}

# invoke url for one record, if you want to put more records replace record with records
invoke_url = "https://v8x2736ebl.execute-api.us-east-1.amazonaws.com/Production/streams/<stream_name>/record"

#To send JSON messages you need to follow this structure
payload = json.dumps({
    "StreamName": "streaming-0e06e68acedb-user",
    "Data": {
            #Data should be send as pairs of column_name:value, with different columns separated by commas
            "ind": record_df["ind"], "first_name": record_df["first_name"], "last_name": record_df["last_name"], "age": record_df["age"],
            "date_joined": record_df["date_joined"]
            },
            "PartitionKey": "ind"
            })

headers = {'Content-Type': 'application/json'}

response = requests.request("PUT", invoke_url, headers=headers, data=payload)

print(response)