from pydantic import BaseModel, Field


class UserIn(BaseModel):
    first_name: str = Field(None)
    last_name: str = Field(None)
    age: int = Field(None)

    class Config:
        orm_mode = True

class UserOut(UserIn):
    id: int
