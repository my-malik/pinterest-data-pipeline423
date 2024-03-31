import requests
from time import sleep
import random
from multiprocessing import Process
import boto3
import json
import sqlalchemy
from sqlalchemy import text
from sqlalchemy import inspect
import pandas as pd


random.seed(100)


class AWSDBConnector:

    def __init__(self):

        self.HOST = "pinterestdbreadonly.cq2e8zno855e.eu-west-1.rds.amazonaws.com"
        self.USER = 'project_user'
        self.PASSWORD = ':t%;yCY3Yjg'
        self.DATABASE = 'pinterest_data'
        self.PORT = 3306
        
    def create_db_connector(self):
        engine = sqlalchemy.create_engine(f"mysql+pymysql://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DATABASE}?charset=utf8mb4")
        return engine

    def list_db_tables(self, engine):
        inspector = inspect(engine) 
        return inspector.get_table_names()

new_connector = AWSDBConnector()

def run_infinite_post_data_loop():
    while True:
        sleep(random.randrange(0, 2))
        random_row = random.randint(0, 11000)
        engine = new_connector.create_db_connector()

        with engine.connect() as connection:

            pin_string = text(f"SELECT * FROM pinterest_data LIMIT {random_row}, 1")
            pin_selected_row = connection.execute(pin_string)
            
            for row in pin_selected_row:
                pin_result = dict(row._mapping)

            geo_string = text(f"SELECT * FROM geolocation_data LIMIT {random_row}, 1")
            geo_selected_row = connection.execute(geo_string)
            
            for row in geo_selected_row:
                geo_result = dict(row._mapping)

            user_string = text(f"SELECT * FROM user_data LIMIT {random_row}, 1")
            user_selected_row = connection.execute(user_string)
            
            for row in user_selected_row:
                user_result = dict(row._mapping)


            invoke_url_pin = "https://v8x2736ebl.execute-api.us-east-1.amazonaws.com/Production/streams/streaming-0e06e68acedb-pin/record"

            payload_pin = json.dumps({
    "StreamName": "streaming-0e06e68acedb-pin",
    "Data": {
    "index": pin_result["index"], "unique_id": pin_result["unique_id"], "title": pin_result["title"], "description": pin_result["description"], "poster_name": pin_result["poster_name"], "follower_count": pin_result["follower_count"], 
       "tag_list": pin_result["tag_list"], "is_image_or_video": pin_result["is_image_or_video"], "image_src": pin_result["image_src"], "downloaded": pin_result["downloaded"], 
       "save_location": pin_result["save_location"], "category": pin_result["category"]},
       "PartitionKey": "index"

})
            

            invoke_url_geo = "https://v8x2736ebl.execute-api.us-east-1.amazonaws.com/Production/streams/streaming-0e06e68acedb-geo/record"

            payload_geo = json.dumps({
    "StreamName": "streaming-0e06e68acedb-geo",
    "Data": {
      "ind": geo_result["ind"], "timestamp": geo_result["timestamp"].strftime("%Y-%m-%d %H:%M:%S"), "latitude": geo_result["latitude"], "longitude": geo_result["longitude"], "country": geo_result["country"]
        },
        "PartitionKey": "ind"
})
            

            invoke_url_user = "https://v8x2736ebl.execute-api.us-east-1.amazonaws.com/Production/streams/streaming-0e06e68acedb-user/record"

            payload_user = json.dumps({
    "StreamName": "streaming-0e06e68acedb-user",
    "Data": {
        "ind": user_result["ind"], "first_name": user_result["first_name"], "last_name": user_result["last_name"], "age": user_result["age"], "date_joined": user_result["date_joined"].strftime("%Y-%m-%d %H:%M:%S")
            },
            "PartitionKey": "ind"
            })
            


        headers = {'Content-Type': 'application/json'}
        response_pin = requests.request("PUT", invoke_url_pin, headers=headers, data=payload_pin, timeout=30)
        response_geo = requests.request("PUT", invoke_url_geo, headers=headers, data=payload_geo, timeout=30)
        response_user = requests.request("PUT", invoke_url_user, headers=headers, data=payload_user, timeout=30)


        print(response_pin,response_geo,response_user)
        print(response_pin.json())
        print(response_geo.json())
        print(response_user.json())





if __name__ == "__main__":
    run_infinite_post_data_loop()
    print('Working')


