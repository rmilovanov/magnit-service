from pydantic import BaseModel, validator
from enum import Enum


class CalcOperations(Enum):
    ADDITION = "+"
    SUBTRACTION = "-"
    MULTIPLICATION = "*"
    DIVISION = "/"


class CalcTaskPayload(BaseModel):
    x: int
    y: int
    operation: str

    @validator("operation")
    def supported_operations(cls, op):
        if op not in CalcOperations._value2member_map_:
            raise ValueError("Supported operations are %s" % list(CalcOperations._value2member_map_.keys()))
        return op


class TaskID(BaseModel):
    id: str


class TaskResult(BaseModel):
    success: bool = True
    result: int
    status: str = "undefined"
