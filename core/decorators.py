import functools
from fastapi import HTTPException
from utils.logger import log_error


def log_errors(func):
    @functools.wraps(func)
    async def wrapper (*args, **kwargs):
        try:
            return await func (*args, **kwargs)
        except Exception as e:
            log_error (str (e))
        