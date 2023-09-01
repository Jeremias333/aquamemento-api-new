from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.trustedhost import TrustedHostMiddleware
import json
from pydantic_settings import BaseSettings
from modules.logger import logger

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