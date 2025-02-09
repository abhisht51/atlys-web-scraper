from functools import wraps
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Request, HTTPException, Depends
from .config import settings

security = HTTPBearer()

def token_required(f):
    @wraps(f)
    async def decorated(request: Request, credentials: HTTPAuthorizationCredentials = Depends(security), *args, **kwargs):
        token = credentials.credentials
        if not token or token != settings.SECRET_TOKEN:
            raise HTTPException(status_code=401, detail="Token is missing or invalid!")
        return await f(request, *args, **kwargs)
    return decorated