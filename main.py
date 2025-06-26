from fastapi import FastAPI
from routers import auth, users, versioning

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(versioning.v1_router, prefix="/v1")
app.include_router(versioning.v2_router, prefix="/v2")

from pydantic import EmailStr, BaseModel
from fastapi import Body

class RegisterRequest(BaseModel):
    email: EmailStr

@app.post("/register")
def register_user(user: RegisterRequest):
    return {"msg": f"{user.email} başarıyla kayıt oldu"}

from typing import Annotated

@app.post("/comment")
def post_comment(comment: Annotated[str, Body(min_length=10, max_length=300)]):
    return {"msg": "Yorum alındı", "comment": comment}

@app.post("/annotated")
def annotated_example(
    name: Annotated[str, Body(min_length=3)],
    age: Annotated[int, Body(ge=18, le=99)]
):
    return {"name": name, "age": age}

@app.post("/email")
def email_check(email: Annotated[EmailStr, Body(...)]):
    return {"email": email}
