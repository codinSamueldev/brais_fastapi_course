from pydantic import BaseModel

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
