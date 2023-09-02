from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.trustedhost import TrustedHostMiddleware
import json
from pydantic_settings import BaseSettings
from modules.logger import logger
from src.classes.controller import ControllerContainer, ControllerPerson, ControllerInfo


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
            "message": "Ocorreu um erro interno: {}".format(e)
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
            "message": "Ocorreu um erro interno: {}".format(e)
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
            "message": "Ocorreu um erro interno: {}".format(e)
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
            "message": "Ocorreu um erro interno: {}".format(e)
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
            "message": "Ocorreu um erro interno: {}".format(e)
        })


@app.get("/api/v1/person/list/")
def person_list(request: Request):
    try:
        controller = ControllerPerson()
        persons = controller.list_all()

        return JSONResponse(status_code=200, content={
            "message": persons
        })
    except ValueError as e:
        return JSONResponse(status_code=500, content={
            "message": "Ocorreu um erro interno: {}".format(e)
        })


@app.get("/api/v1/person/get/{id}")
def person_get(request: Request, id):
    try:
        controller = ControllerPerson()
        person = controller.get_by_id(id)

        return JSONResponse(status_code=200, content={
            "message": person
        })
    except ValueError as e:
        return JSONResponse(status_code=500, content={
            "message": "Ocorreu um erro interno: {}".format(e)
        })


@app.post("/api/v1/person/create/")
async def person_create(request: Request):
    try:
        body = await request.body()
        body = json.loads(body)

        controller = ControllerPerson()
        controller.create(body['name'], body['kg'])

        return JSONResponse(status_code=200, content={
            "message": body
        })
    except ValueError as e:
        return JSONResponse(status_code=500, content={
            "message": "Ocorreu um erro interno: {}".format(e)
        })


@app.post("/api/v1/person/set_drink/")
async def person_set_drink(request: Request):
    try:
        body = await request.body()
        body = json.loads(body)

        controller = ControllerPerson()
        controller.set_drink(body['person_id'], body['info_id'])

        return JSONResponse(status_code=200, content={
            "message": body
        })
    except ValueError as e:
        return JSONResponse(status_code=500, content={
            "message": "Ocorreu um erro interno: {}".format(e)
        })


@app.get("/api/v1/info/list/")
def info_list(request: Request):
    try:
        controller = ControllerInfo()
        infos = controller.list_all()

        return JSONResponse(status_code=200, content={
            "message": infos
        })
    except ValueError as e:
        return JSONResponse(status_code=500, content={
            "message": "Ocorreu um erro interno: {}".format(e)
        })


@app.get("/api/v1/info/get/{id}")
def info_get(request: Request, id):
    try:
        controller = ControllerInfo()
        info = controller.get_by_id(id)

        return JSONResponse(status_code=200, content={
            "message": info
        })
    except ValueError as e:
        return JSONResponse(status_code=500, content={
            "message": "Ocorreu um erro interno: {}".format(e)
        })


@app.post("/api/v1/info/create/")
async def info_create(request: Request):
    try:
        body = await request.body()
        body = json.loads(body)

        controller = ControllerInfo()
        controller.create(
            body['drank'], body['reached_goal'], body['person_id'])

        return JSONResponse(status_code=200, content={
            "message": body
        })
    except ValueError as e:
        return JSONResponse(status_code=500, content={
            "message": "Ocorreu um erro interno: {}".format(e)
        })


@app.get("/api/v1/info/history/{person_id}/")
def info_list_by_person(request: Request, person_id):
    try:
        controller = ControllerInfo()
        infos = controller.list_all_by_person(person_id)

        return JSONResponse(status_code=200, content={
            "message": infos
        })
    except ValueError as e:
        return JSONResponse(status_code=500, content={
            "message": "Ocorreu um erro interno: {}".format(e)
        })

@app.get("/api/v1/info/today/{person_id}/")
def info_list_by_person(request: Request, person_id):
    try:
        controller = ControllerInfo()
        infos = controller.get_info_for_today(person_id)

        return JSONResponse(status_code=200, content={
            "message": infos
        })
    except ValueError as e:
        return JSONResponse(status_code=500, content={
            "message": "Ocorreu um erro interno: {}".format(e)
        })

@app.post("/api/v1/info/consume/")
async def info_consume(request: Request):
    try:
        body = await request.body()
        body = json.loads(body)

        controller = ControllerInfo()
        value = controller.consume_drink(body['info_id'], body['ml'])

        return JSONResponse(status_code=200, content={
            "message": value
        })
    except ValueError as e:
        return JSONResponse(status_code=500, content={
            "message": "Ocorreu um erro interno {}".format(e)
        })

@app.get("/api/v1/info/remaning/{info_id}/")
def info_remaning(request: Request, info_id):
    try:
        controller = ControllerInfo()
        value = controller.remaning_goal(info_id)

        return JSONResponse(status_code=200, content={
            "message": value
        })
    except ValueError as e:
        return JSONResponse(status_code=500, content={
            "message": "Ocorreu um erro interno {}".format(e)
        })

@app.get("/api/v1/info/remaning/goal/percent/{info_id}/")
def info_remaning_percent(request: Request, info_id):
    try:
        controller = ControllerInfo()
        value = controller.remaning_goal_percent(info_id)

        return JSONResponse(status_code=200, content={
            "message": value
        })
    except ValueError as e:
        return JSONResponse(status_code=500, content={
            "message": "Ocorreu um erro interno {}".format(e)
        })