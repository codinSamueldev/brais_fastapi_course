from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from db.schemas.user import user_schema, users_schema
from db.models.user import User
from db.client import db_client
#
from bson import ObjectId

router = APIRouter(prefix="/usersdb", 
                   tags=["Users DB"], 
                   responses={404: {"message": "Not Found"}})


users_list = []


def search_user(field: str, key):
    try:
        # Find user's email in order to prevent have same email in the db
        user = db_client.local.users.find_one({field: key})
        # Return all elements in the user_schema()
        return User(**user_schema(user))
    except:
        return JSONResponse(content={"404":"Not found"}, status_code=404)


@router.get('/', response_model=list[User])
async def users():
    return users_schema(db_client.local.users.find())

# Path parameter.
@router.get('/{id}', status_code=200)
async def user(id: str):
    return search_user("_id", ObjectId(id))
    
""" 
We can retrieve information with a path parameter such as id, 
or with a query such as id, name, last_name, etc. 
Either way, both are possible
"""

# Query parameters
@router.get('/', status_code=200)
async def user_query(id: str | None = None):
    return search_user("_id", ObjectId(id))


# POST
@router.post('/', status_code=201, response_model=User)
async def new_user(user: User):
    
    # If email is already stored, raise error.
    if type(search_user("email", user.email)) == User:
        raise HTTPException(status_code=422, detail="User already exists")
   
    # If not, then store new user values and delete its id
    user_dict = dict(user)
    del user_dict["id"]

    # Store new user id in the users schema.
    id = db_client.local.users.insert_one(user_dict).inserted_id

    # Then, find id 
    new_user = user_schema(db_client.local.users.find_one({"_id": id}))

    return User(**new_user)


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


