from fastapi import APIRouter, HTTPException
from starlette import status
from starlette.requests import Request

from src.routers import routes
from src.templates import render_template

main_router = APIRouter()
main_router.include_router(routes.routes_router)


@main_router.get('/')
def home(request: Request):
    return render_template('index.html', request=request)


@main_router.get('/{catchall:path}')
async def catch_all():
    raise HTTPException(status_code=status.HTTP_307_TEMPORARY_REDIRECT, detail="Temporary Redirect",
                        headers={"Location": "/"})
