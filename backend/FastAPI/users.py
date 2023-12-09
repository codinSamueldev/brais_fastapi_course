from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
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


def get_user(id: int):
    # For each element in user_list, filter each one if the id matches.
    user = filter(lambda user: user.id == id, users_list)
    try:
        return list(user)[0]
    except:
        return JSONResponse(content={"404":"Not found"}, status_code=404)


@app.get('/usersjson', tags=["JSON Users"])
async def usersjson():
    return [{"name": "Samuel", "last name": "Henao", "nickname": "csamueldev", "Programmer": True}, 
            {"name": "Alpaca", "last name": "Gonzales", "nickname": "alpacor", "Programmer": False}, 
            {"name": "Alberto", "last name": "Ramirez", "nickname": "albertico", "Programmer": False}]


@app.get('/users', tags=["Users"])
async def usersclass():
    # return entity
    return users_list

# Path parameter.
@app.get('/user/{id}', tags=["Users"], status_code=200)
async def user(id: int):
    return get_user(id)
    
""" 
We can retrieve information with a path parameter such as id, 
or with a query such as id, name, last_name, etc. 
Either way, both are possible
"""

# Query parameters
@app.get('/user/', tags=["Users"], status_code=200)
async def user_query(id: int):
    return get_user(id)
