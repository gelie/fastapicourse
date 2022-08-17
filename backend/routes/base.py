from fastapi import APIRouter
from routes.api.version1 import route_users, route_jobs, route_login
from routes.web import route_web

api_router = APIRouter()

api_router.include_router(router=route_users.router)
api_router.include_router(router=route_jobs.router)
api_router.include_router(router=route_login.router)
api_router.include_router(router=route_web.router)
