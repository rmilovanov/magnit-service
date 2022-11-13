import os
import time

from celery import Celery


celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")


@celery.task(name="create_task")
def make_computations(data):
    ops = {
        "+": "__add__",
        "-": "__sub__",
        "*": "__mul__",
        "/": "__truediv__",
    }

    func = getattr(data["x"], ops[data["operation"]])
    return func(data["y"])

