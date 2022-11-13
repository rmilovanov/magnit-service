import logging

from celery.result import AsyncResult
from fastapi import FastAPI
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator

from service.schemas import CalcTaskPayload, TaskID, TaskResult
from service.worker import make_computations


logging.basicConfig(filename="log.log", level=logging.INFO)


app = FastAPI(
    title="Magnit Test API",
    version="0.0.1",
    contact={
        "name": "Roman Milovanov",
        "url": "https://t.me/atlasmaster",
    },
)


@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")


@app.post("/calc/", response_model=TaskID)
async def calc(data: CalcTaskPayload):
    task = make_computations.delay(data.dict())
    return TaskID(id=task.id)


@app.get("/task/{task_id}/", response_model=TaskResult)
async def task_result(task_id: str):
    task_res = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_res.status,
        "task_result": task_res.result,
    }
    return JSONResponse(result)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Instrumentator().instrument(app).expose(app)
