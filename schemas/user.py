from pydantic import BaseModel,EmailStr

class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserResponseSchema(BaseModel):
    id: int
    username: str
    email: EmailStr
    