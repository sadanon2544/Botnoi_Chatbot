from fastapi import APIRouter
from model.models import line_user
from config.db import collection_line, collection_account

lineRouter = APIRouter()

@lineRouter.post("/post", tags=["user"])
async def post_users(user: line_user):
    collection_line.insert_one(dict(user))
    return {"status": "OK"}

@lineRouter.post("/finduser/{id}", tags=["user"])
async def get_one_user(id: str):
    user = collection_account.find_one({"sub": id}, {'_id': False})
    return {"status": "OK", "data":user}
