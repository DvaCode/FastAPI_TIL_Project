# user/interface/controllers/user_controller.py
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Annotated
from user.application.user_service import UserService
from dependency_injector.wiring import inject, Provide
from containers import Conatiner
router = APIRouter(prefix="/users")

class CreateUserBody(BaseModel):
    name: str
    email: str
    password: str

@router.post("", status_code=201)
@inject
def create_user(
    user: CreateUserBody,
    user_service: UserService = Depends(Provide[Conatiner.user_service]),
    ):
    user_service = UserService()
    created_user = user_service.create_user(
        name = user.name,
        email = user.email,
        password = user.password
    )
    
    return created_user