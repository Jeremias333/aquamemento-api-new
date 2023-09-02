from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.trustedhost import TrustedHostMiddleware
import json
from pydantic_settings import BaseSettings
from modules.logger import logger
from src.controller import ControllerContainer

class Settings(BaseSettings):
    app_name: str = "Aquamemento API"
    port_default: int = 8000

settings = Settings()
app = FastAPI()

print("       SERVICE: {}".format(settings.app_name))
logger.log("{} - inicializado.".format(settings.app_name))

app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=["127.0.0.1", "*"]
)


@app.get("/")
def index():
    try:
        return JSONResponse(status_code=200, content={
            "message": "Hello Planet"
        })
    except ValueError as e:
        logger.log("Ocorreu um erro durante o acesso {}".format(e), "ERROR")
        return JSONResponse(status_code=500, content={
            "message":"Ocorreu um erro interno: {}".format(e)
        })

@app.post("/api/v1/")
async def route(request: Request):
    try:
        body = await request.body()
        body = json.loads(body)

        return JSONResponse(status_code=200, content={
            "message": body
        })
    except ValueError as e:
        logger.log("Ocorreu um erro: {}".format(e), "ERROR | SERVICE1")

        return JSONResponse(status_code=500, content={
            "message":"Ocorreu um erro interno: {}".format(e)
        })

@app.post("/api/v1/container/create/")
async def container_create(request: Request):
    try:
        body = await request.body()
        body = json.loads(body)

        controller = ControllerContainer()
        controller.create(body['title'], body['capacity'])

        return JSONResponse(status_code=200, content={
            "message": body
        })
    except ValueError as e:
        return JSONResponse(status_code=500, content={
            "message":"Ocorreu um erro interno: {}".format(e)
        })

@app.get("/api/v1/container/list/")
def container_list(request: Request):
    try:
        controller = ControllerContainer()
        containers = controller.list_all()

        return JSONResponse(status_code=200, content={
            "message": containers
        })
    except ValueError as e:
        return JSONResponse(status_code=500, content={
            "message":"Ocorreu um erro interno: {}".format(e)
        })

@app.get("/api/v1/container/get/{id}")
def container_get(request: Request, id):
    try:
        controller = ControllerContainer()
        container = controller.get_by_id(id)

        return JSONResponse(status_code=200, content={
            "message": container
        })
    except ValueError as e:
        return JSONResponse(status_code=500, content={
            "message":"Ocorreu um erro interno: {}".format(e)
        })