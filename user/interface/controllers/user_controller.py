# user/interface/controllers/user_controller.py
from fastapi import APIRouter
from pydantic import BaseModel, EmailStr
from user.application.user_service import UserService
from user.domain.user import Profile
router = APIRouter(prefix="/users")

class CreateUserBody(BaseModel):
    profile: Profile
    password: str

@router.post("", status_code=201)
def create_user(user: CreateUserBody):
    user_service = UserService()
    created_user = user_service.create_user(
        profile = user.profile,
        password = user.password
    )
    
    return created_user