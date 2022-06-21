from pydantic import BaseModel, Field
from typing import List, Union, Any


class CustomHttpModel(BaseModel):
    response: Any


class PaginateModel(CustomHttpModel):
    response: List[Any]
    previous_page: Union[int, None]
    next_page: Union[int, None]
    has_previous: Union[bool, None]
    has_next: Union[bool, None]
    total: Union[int, None]
    pages: Union[int, None]


class CustomHttpErrorModel(BaseModel):
    detail: str = Field(
        description="Description of the specific error handled. In addition, there is a specifier at the beginning of the message indicating what was the exception type")


class ParamsVerifError(BaseModel):
    loc: List[str] = Field(
        description="Location of specific invalid parameter")
    msg: str = Field(description="Description")
    type: str = Field(description="Expected value type or error type")


class ParamsErrorModel(BaseModel):
    detail: List[ParamsVerifError]
