""" File to init FastAPI """
import os
import time
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.apis.routes import route as route_apis
from app.apis.master.router import router as master_router
from libraries.translator.translator import Traslator

app = FastAPI(
    docs_url="/docs",
    redoc_url="/redocs",
    title="APIs - My Finances",
    description="Esta web documenta las APIs del proyecto mis finanzas",
    version="1.0",
    openapi_url="/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex='https?://.*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=['Content-Type', 'Authorization', 'Requester'],
)

Traslator.load_translations()
route_apis(app)

if os.environ['APP_MODE'] != "production":
    app.include_router(master_router, tags=["Master"])

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    """ Calculates time on execute APIs """
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers['X-Process-Time'] = str(process_time)
    return response

@app.get("/")
async def get():
    """ Response / """
    return "Hola Mundo"
