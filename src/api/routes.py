from fastapi import APIRouter, Depends, Header, HTTPException
from ..core.config import settings

router = APIRouter()


def verify_token(x_token: str = Header(...)):
    if x_token != settings.SECRET_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid token")


@router.get("/ping", response_model=None)
def ping():
    return "PONG"
