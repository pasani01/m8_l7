from fastapi import APIRouter

router = APIRouter(prefix="/auth",tags=['log in'])

@router.post("/login")
def login():
    return {"msg": "Giriş yapıldı"}

@router.post("/logout")
def logout():
    return {"msg": "Çıkış yapıldı"}
