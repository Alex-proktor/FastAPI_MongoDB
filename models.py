import json

from pymongo import MongoClient

from settings import *


class Users:
    def __init__(self, db_name=DB_NAME):
        conn = MongoClient(HOST, PORT)

        db = conn.mydb
        self.coll = db[db_name]

    def json_to_mongo(self, file_name=JSON_DAMP):
        try:
            with open(file_name, 'r') as json_file:
                data = json.load(json_file)
                for item in data:
                    self.send(item)

                print(data)
        except ImportError:
            raise Exception(f'ERROR: {JSON_DAMP} file not found')

    def send(self, item):
        self.coll.insert_one(item)

    async def get(self, *args, **kwargs):
        request = {}
        for key, val in kwargs.items():
            if val:
                request[key] = val

        response = []
        for item in self.coll.find(request):
            item.pop('_id')
            response.append(item)

        return response

    def clean_out(self):
        self.coll.remove({})


if __name__ == '__main__':
    print('start')

    us = Users()
    user = us.get(company='Yandex', age=26, name=None)
