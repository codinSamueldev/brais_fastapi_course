from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

router = APIRouter(prefix="/usersdb", 
                   tags=["Users DB"], 
                   responses={404: {"message": "Not Found"}})

# Base model allows to create entities.
class User(BaseModel):
    id: int
    name: str
    last_name : str
    nickname: str
    programmer: bool

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 999,
                    "name": "Juan",
                    "last_name": "Gonzales",
                    "nickname": "juanito",
                    "programmer": True
                }
            ]
        }
    }


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


@router.get('/usersjson')
async def usersjson():
    return [{"name": "Samuel", "last name": "Henao", "nickname": "csamueldev", "Programmer": True}, 
            {"name": "Alpaca", "last name": "Gonzales", "nickname": "alpacor", "Programmer": False}, 
            {"name": "Alberto", "last name": "Ramirez", "nickname": "albertico", "Programmer": False}]


@router.get('/')
async def users():
    # return entity
    return users_list

# Path parameter.
@router.get('/{id}', status_code=200)
async def user(id: int):
    return get_user(id)
    
""" 
We can retrieve information with a path parameter such as id, 
or with a query such as id, name, last_name, etc. 
Either way, both are possible
"""

# Query parameters
@router.get('/', status_code=200)
async def user_query(id: int | None = None):
    return get_user(id)


# POST
@router.post('/', status_code=201, response_model=User)
async def new_user(user: User):
    if type(get_user(user.id)) == User:
        raise HTTPException(status_code=422, detail="User already exists")
    else:
        user_created = users_list.append(user)
        return JSONResponse(status_code=201, content=user_created)


# PUT
@router.put('/{id}', status_code=200)
async def update_user(user: User):
    for position, users_saved in enumerate(users_list):
        if users_saved.id == user.id:
            users_list[position] = user
        
    return user


# DELETE
@router.delete('/{id}', status_code=200)
async def delete_user(id: int):

    found = False

    for user in users_list:
        if user.id == id:
            users_list.remove(user)
            found = True
            return {"message": f"user {user.name} deleted"}
    
    if user.id not in users_list:
        raise HTTPException(status_code=400, detail=f"user {id} does not exist.")


