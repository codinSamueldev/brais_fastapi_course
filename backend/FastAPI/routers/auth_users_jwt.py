from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta


ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1
# Command: openssl rand -hex 32
SECRET = "4a4375fb6aa556852f2cc534620abf4ac3c17c0819caa8d46efd15ea53107947"


router = APIRouter()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes=["bcrypt"])

class User(BaseModel):
    username: str
    name: str
    email: str
    disable: bool


class UserDB(User):
    password: str


users_db = {
    "codinsamueldev": {
        "username": "codinsamueldev",
        "name": "Samuel",
        "email": "csamueldev@yopmail.com",
        "disable": False,
        "password": "$2a$12$rbcVUDb0g7GrsLMd1/7.suLaLQ16GkXoXS832hBMWNhkbeSwDYmVW"
    },
    "alpachino": {
        "username": "alpachino",
        "name": "Alpaca",
        "email": "alpacadev@yopmail.com",
        "disable": True,
        "password": "$2a$12$3T9/ImV2pxzwqfODGPVpOOaMA6UXY7sNQxPTF5SHq0JVwEtGS.sYW"
    }
}


def search_user_db(password: str):
    if password in users_db:
        return UserDB(**users_db[password])


def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])


async def auth_user(token: str = Depends(oauth2)):
    # Assign error to a var so as to use it several times
    exception = HTTPException(status_code=401, 
                            detail={"message": f"Invalid auth credentials."},
                            headers={"WWW-Authenticate": "Bearer"})

    try:
        # Decode token, and return username.
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        # If user does not exist, raise error.
        if username is None:
            raise exception
    except JWTError:
        raise exception
    
    # After all validations, return username
    return search_user(username)


async def current_user(user: User = Depends(auth_user)):
    # Validate if user is disable 
    if user.disable:
        raise HTTPException(status_code=406, 
                            detail={"message": "User not active."})
    
    return user


@router.post('/login', tags=["Auth"])
async def login(form: OAuth2PasswordRequestForm = Depends()):
    # Validate user it is registered in the database.
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=400, 
                            detail={"message": "User is not registered"})
    
    # Verify user type correct password.
    user = search_user_db(form.username)

    if not crypt.verify(form.password, user.password):
        raise HTTPException(status_code=400, 
                            detail={"message": "Wrong password"})

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)

    # Usually, sub takes the userId, however our db at this moment has as id the username.
    access_token = {"sub": user.username, "exp": expire}

    return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM), "token_type": "bearer"}


@router.get('/users/me', tags=["Auth"])
async def me(user: User = Depends(current_user)):
    return user
