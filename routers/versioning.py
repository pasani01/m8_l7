from fastapi import APIRouter

v1_router = APIRouter(tags=['status'])

@v1_router.get("/status")
def status_v1():
    return {"version": "1", "status": "OK"}

v2_router = APIRouter(tags=['status'])

@v2_router.get("/status")
def status_v2():
    return {"version": "2", "status": "İyi"}
