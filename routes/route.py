from fastapi import APIRouter
from modals.todos import ToDo
from config.database import collection_name
from schema.schemas import list_serial, individual_serial
from bson import ObjectId

router = APIRouter()

# GET request method
# Get all the data from the collection
@router.get('/todos')
async def get_all_todos():
    todos = list_serial(collection_name.find())
    return todos

# GET request method
# Get selected data from the collection
@router.get('/todo/{id}')
async def get_todo_by_id(id: str):
    todo = individual_serial(collection_name.find_one({'_id': ObjectId(id)}))
    return todo

# POST request method
@router.post('/todos')
async def create_todo(todo: ToDo):
    collection_name.insert_one(dict(todo))
    return todo

# PUT request method
@router.put('/todo/{id}')
async def update_todo(id: str, todo: ToDo):
    collection_name.find_one_and_update({'_id': ObjectId(id)}, {'$set': dict(todo)})
    return todo

# DELETE request method
@router.delete('/todo/{id}')
# Delete selected data from the collection
async def delete_todo_by_id(id: str):
    collection_name.find_one_and_delete({'_id': ObjectId(id)})
    return 0

# DELETE request method
# Delete all the data from the collection
@router.delete('/todos')
async def delete_all_todos():
    collection_name.delete_many({})
    return 0