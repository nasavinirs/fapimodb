import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

server = os.getenv('SERVER')
app_name = os.getenv('APP_NAME')
db_username = os.getenv('DB_USERNAME')
db_password = os.getenv('DB_PASSWORD')

uri = f'mongodb+srv://{db_username}:{db_password}@{server}/?retryWrites=true&w=majority&appName={app_name}'
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.todo_db

collection_name = db['todo_collection']