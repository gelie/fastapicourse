from fastapi import APIRouter
from api.version1 import route_users, route_jobs, route_login, route_web

api_router = APIRouter()

api_router.include_router(router=route_users.router, prefix="/users", tags=["users"])
api_router.include_router(router=route_jobs.router, prefix="/jobs", tags=["jobs"])
api_router.include_router(router=route_login.router, prefix="/login", tags=["login"])
api_router.include_router(router=route_web.router, prefix="", tags=["web ui"])
