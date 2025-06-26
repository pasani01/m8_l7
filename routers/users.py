from fastapi import APIRouter
from pydantic import BaseModel, EmailStr, Field
from typing import Annotated

router = APIRouter(tags=['user create'])

class UserData(BaseModel):
    name: Annotated[str, Field(min_length=3)]
    email: Annotated[EmailStr, Field(description="Geçerli email adresi")]
    age: Annotated[int, Field(ge=18, le=99)]

@router.post("/users/create")
def create_user(user: UserData):
    return {"msg": "Kullanıcı oluşturuldu", "user": user}
