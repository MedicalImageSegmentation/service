from fastapi import HTTPException
from google.protobuf.empty_pb2 import Empty

from api.medicalImagesegmentation.user.user_pb2 import LoginRequest, DoctorInfo, DoctorId, GetDoctorListRequest, \
    DoctorName
from api.medicalImagesegmentation.user.user_pb2_http import UserServicer, register_user_http_server
from core.app import instance
from core.router_register import request_context, register_fastapi_route, parse_request, parse_reply
from dao.user_dao import verify_user_password
from modules.JWTUtilTest import UserContext


class DoctorServiceImpl(UserServicer):
    async def Login(self, request: LoginRequest) -> Empty:
        session = instance.database.get_db_session()
        doctor = verify_user_password(request.name, request.psw, session)
        if doctor is None:
            raise HTTPException(status_code=404, detail="User not exist")

        request_context.set(UserContext(userid=doctor.id))

        return Empty()

    async def AddDoctorInfo(self, request: DoctorInfo) -> DoctorId:
        pass

    async def ModifyDoctorInfo(self, request: DoctorInfo) -> DoctorId:
        pass

    async def GetDoctorList(self, request: Empty) -> GetDoctorListRequest:
        pass

    async def GetDoctorInfoByName(self, request: DoctorName) -> GetDoctorListRequest:
        pass

    async def GetDoctorInfoById(self, request: DoctorId) -> GetDoctorListRequest:
        pass


register_user_http_server(register_fastapi_route, DoctorServiceImpl(), parse_request, parse_reply)
