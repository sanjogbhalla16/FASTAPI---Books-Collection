from fastapi import APIRouter, HTTPException
from schemas.user import UserSchema, UserResponseSchema

user_router = APIRouter()

@user_router.post("/user_register", response_model=UserResponseSchema)
def user_register(user: UserSchema):
    # Logic for user registration
    return {"message": "User registered successfully"}

@user_router.post("/user_login")
def user_login(user: UserSchema):
    # Logic for user login
    return {"message": "User logged in successfully"}
