import uvicorn
from fastapi import FastAPI
import logging
from service.schemas import CalcTaskPayload, TaskID, TaskResult
# from computations import make_computation, assign_task_id, StoreTasks
from service.worker import make_computations
from celery.result import AsyncResult
from fastapi.responses import JSONResponse
from fastapi.responses import RedirectResponse


logging.basicConfig(filename="log.log", level=logging.INFO)


app = FastAPI(
    title="Magnit Test API",
    version="0.0.1",
    contact={
        "name": "Roman Milovanov",
        "url": "https://t.me/atlasmaster",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)


@app.get("/", include_in_schema=False)
async def root():
    # return {"message": "Server up and running in docker!"}
    return RedirectResponse(url='/docs')


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
        "task_result": task_res.result
    }
    return JSONResponse(result)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
