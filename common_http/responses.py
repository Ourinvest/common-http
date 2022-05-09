from fastapi import status, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import Response, JSONResponse
from common_http.definitions import DICT_REQUEST_RESPONSES
from common_http.schemas import *


class CustomResponse:
    @staticmethod
    def success(response):
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "response": jsonable_encoder(response),
            },
        )

    @staticmethod
    def created(response):
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={
                "response": jsonable_encoder(response),
            },
        )

    @staticmethod
    def not_content():
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    @staticmethod
    def partial_content(
        response, previous_page, next_page, has_previous, has_next, total, pages
    ):
        return JSONResponse(
            status_code=status.HTTP_206_PARTIAL_CONTENT,
            content={
                "response": jsonable_encoder(response),
                "previous_page": previous_page,
                "next_page": next_page,
                "has_previous": has_previous,
                "has_next": has_next,
                "total": total,
                "pages": pages,
            },
        )

    @staticmethod
    def custom_response(status_code, response):
        return JSONResponse(
            status_code=status_code,
            content={
                "response": jsonable_encoder(response),
            }
        )

    @staticmethod
    def bad_request(error_detail):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"BAD REQUEST: {error_detail}",
        )

    @staticmethod
    def conflict(error_detail):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail=f"CONFLICT: {error_detail}"
        )

    @staticmethod
    def gone():
        raise HTTPException(
            status_code=status.HTTP_410_GONE, detail="GONE: Object no longer exists"
        )

    @staticmethod
    def server_error(detail):
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"INTERNAL SERVER FAIL: {detail}",
        )

    @staticmethod
    def custom_error(status_code, detail):
        raise HTTPException(status_code=status_code, detail=f"{detail}")


def get_possible_responses(request_type: str, codes: list):
    response = {}
    dict_responses = DICT_REQUEST_RESPONSES.get(request_type.lower(), {})
    for code in codes:
        response.update({code: dict_responses.get(code, {})})
    return response
