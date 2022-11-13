from enum import Enum
from pydantic import BaseModel, validator


class CalcOperations(Enum):
    ADDITION = "+"
    SUBTRACTION = "-"
    MULTIPLICATION = "*"
    DIVISION = "/"

    @classmethod
    def members(cls):
        return list(cls._value2member_map_.keys())


class CalcTaskPayload(BaseModel):
    x: int
    y: int
    operation: str

    @validator("operation")
    def supported_operations(self, oprtn):  # cls?
        if oprtn not in CalcOperations.members():
            raise ValueError(f"Supported operations are {CalcOperations.members()}")
        return oprtn


class TaskID(BaseModel):
    id: str


class TaskResult(BaseModel):
    success: bool = True
    result: int
    status: str = "undefined"
