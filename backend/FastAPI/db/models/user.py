from pydantic import BaseModel

class User(BaseModel):
    id: str | None = None
    username: str
    email : str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 999,
                    "username": "juano",
                    "email": "jhondoe@yopmail.com"
                }
            ]
        }
    }
