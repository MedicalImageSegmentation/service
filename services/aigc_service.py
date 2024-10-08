import aiohttp as aiohttp
import requests
from google.protobuf.empty_pb2 import Empty

from api.medicalImagesegmentation.aigc.aigc_pb2 import FileHash
from api.medicalImagesegmentation.aigc.aigc_pb2_http import AigcServicer, register_aigc_http_server
from core.router_register import register_fastapi_route, parse_request, parse_reply


async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


class AigcService(AigcServicer):
    async def ModelHandle(self, request: FileHash) -> Empty:
        response = await fetch_data("http://124.222.0.214:1234/pridict/" + request.hash)
        return Empty()


register_aigc_http_server(register_fastapi_route, AigcService(), parse_request, parse_reply)
