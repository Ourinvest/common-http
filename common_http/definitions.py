from common_http.schemas import *

BASE_RESPONSES = {
    400: {
        "model": CustomHttpErrorModel,
        "description": "Paramenter value given is not valid",
    },
    401: {
        "model": CustomHttpErrorModel,
        "description": "User has no access rights to perform query",
    },
    403: {
        "model": CustomHttpErrorModel,
        "description": "User has no access rights to endpoint",
    }
}

GET_RESPONSES = {
    200: {
        "model": CustomHttpModel,
        "description": "Query for objects performed successfully",
    },
    204: {"description": "Object not found"},
    206: {
        "model": CustomHttpErrorModel,
        "description": "List of objects returned in pages.",
    },
    **BASE_RESPONSES
}

POST_RESPONSES = {
    201: {"model": CustomHttpModel, "description": "Object created succesffully"},
    202: {
        "model": CustomHttpModel,
        "description": "Request accepted but not processed yet",
    },
    409: {
        "model": CustomHttpErrorModel,
        "description": "Object already registered",
    },
    422: {
        "model": ParamsErrorModel,
        "description": "Parameters for creation not valid",
    },
    **BASE_RESPONSES,
}

PUT_RESPONSES = {
    200: {"model": CustomHttpModel, "description": "Object updated successfully"},
    202: {
        "model": CustomHttpModel,
        "description": "Request accepted but not processed yet",
    },
    404: {"model": CustomHttpErrorModel, "description": ""},
    409: {"model": CustomHttpErrorModel, "description": ""},
    410: {"model": CustomHttpErrorModel, "description": "Object no longer exists"},
    422: {
        "model": ParamsErrorModel,
        "description": "Parameters for creation not valid",
    },
    **BASE_RESPONSES,
}

DELETE_RESPONSES = {
    200: {"model": CustomHttpModel, "description": "Action performed successfully"},
    204: {"description": "Deleted successfully"},
    410: {"model": CustomHttpErrorModel, "description": "Object no longer exists"},
    **BASE_RESPONSES,
}

DICT_REQUEST_RESPONSES = {
    "get": GET_RESPONSES,
    "post": POST_RESPONSES,
    "put": PUT_RESPONSES,
    "delete": DELETE_RESPONSES,
}
