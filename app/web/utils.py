import typing

from aiohttp.web import json_response as aiohttp_json_response
from aiohttp.web_response import Response


def json_response(data: typing.Any = None, status: str = "ok") -> Response:
    if data is None:
        data = {}
    return aiohttp_json_response(
        data={
            "status": status,
            "data": data,
        }
    )


def error_json_response(
    http_status: int,
    status: str = "error",
    message: typing.Optional[str] = None,
    data: typing.Optional[dict] = None,
) -> typing.Any:
    if data is None:
        data = {}
    return aiohttp_json_response(
        status=http_status, data={"status": status, "message": message, "data": data}
    )
