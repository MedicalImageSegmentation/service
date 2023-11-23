from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

from api.medicalImagesegmentation.ping.ping_pb2 import pong
from api.medicalImagesegmentation.ping.ping_pb2_http import PingServicer, register_ping_http_server
from core.app import instance
from core.router_register import register_fastapi_route, parse_reply, parse_request
from modles.file_entity import FileEntity


class PingServiceImpl(PingServicer):
    async def Ping(self, request: google_dot_protobuf_dot_empty__pb2.Empty) -> pong:
        return pong(msg="pong")


register_ping_http_server(register_fastapi_route, PingServiceImpl(), parse_request, parse_reply)
