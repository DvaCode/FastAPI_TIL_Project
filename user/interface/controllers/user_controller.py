# user/interface/controllers/user_controller.py
from fastapi import APIRouter
from pydantic import BaseModel, EmailStr
from user.application.user_service import UserService
router = APIRouter(prefix="/users")

class ProfileSchema(BaseModel):
    name: str
    email: EmailStr
    class Config:
        orm_mode = True

class CreateUserBody(BaseModel):
    profile: ProfileSchema
    password: str

@router.post("", status_code=201)
def create_user(user: CreateUserBody):
    user_service = UserService()
    created_user = user_service.create_user(
        profile = user.profile,
        password = user.password
    )
    
    return created_user