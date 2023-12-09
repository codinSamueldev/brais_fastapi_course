from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Base model allows to create entities.
class User(BaseModel):
    id: int
    name: str
    last_name : str
    nickname: str
    programmer: bool


users_list = [User(id=0, name="Samuel", last_name="Henao", nickname="csamueldev", programmer=True),
         User(id=1, name="Alpaca", last_name="Gonzales", nickname="alpacor", programmer=False),
         User(id=2, name="Alberto", last_name="Ramirez", nickname="albertico", programmer=False)]


@app.get('/usersjson', tags=["JSON Users"])
async def usersjson():
    return [{"name": "Samuel", "last name": "Henao", "nickname": "csamueldev", "Programmer": True}, 
            {"name": "Alpaca", "last name": "Gonzales", "nickname": "alpacor", "Programmer": False}, 
            {"name": "Alberto", "last name": "Ramirez", "nickname": "albertico", "Programmer": False}]


@app.get('/users', tags=["Users"])
async def usersclass():
    # return entity
    return users_list

# Use parameter.
@app.get('/user/{id}', tags=["Users"])
async def user(id: int):
    return users_list
