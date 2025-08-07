from api.user_management.model import RegisterRequest
from api.user_management.service import register_user
from core.decorators import log_errors
from fastapi import APIRouter, Depends


router = APIRouter()

router.post("/register")
@log_errors
async def register (req: RegisterRequest):
    return register_user(req) 