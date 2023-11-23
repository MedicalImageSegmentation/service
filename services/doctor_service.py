from fastapi import HTTPException
from google.protobuf.empty_pb2 import Empty

from api.medicalImagesegmentation.user.user_pb2 import LoginRequest, DoctorInfo, DoctorId, GetDoctorListRequest, \
    DoctorName
from api.medicalImagesegmentation.user.user_pb2_http import UserServicer, register_user_http_server
from core.app import instance
from core.router_register import request_context, register_fastapi_route, parse_request, parse_reply
from dao.user_dao import verify_user_password, create_doctor_info, verify_user_is_admin, modify_doctor_info, \
    get_all_doctor_info, get_doctor_info_by_name, get_doctor_info_by_id
from modles.doctor_entity import DoctorEntity
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
        session = instance.database.get_db_session()
        is_admin = verify_user_is_admin(request_context.get().userid, session)
        if is_admin is False:
            raise HTTPException(status_code=403, detail="Forbidden")

        doctor = create_doctor_info(DoctorEntity(
            sex=request.sex,
            name=request.name,
            password=request.psw,
            id_number=request.id_card,
            phone=request.phone,
            department=request.department,
            avatar_image=request.img_id,
            is_admin=request.is_admin,
            title=request.title
        ), session)
        return DoctorId(id=doctor.id)

    async def ModifyDoctorInfo(self, request: DoctorInfo) -> DoctorId:
        session = instance.database.get_db_session()
        is_admin = verify_user_is_admin(request_context.get().userid, session)
        if is_admin is False:
            raise HTTPException(status_code=403, detail="Forbidden")

        doctor = modify_doctor_info(DoctorEntity(
            sex=request.sex,
            name=request.name,
            password=request.psw,
            id_number=request.id_card,
            phone=request.phone,
            department=request.department,
            avatar_image=request.img_id,
            is_admin=request.is_admin,
            title=request.title
        ), session)

        return DoctorId(id=doctor.id)

    async def GetDoctorList(self, request: Empty) -> GetDoctorListRequest:
        session = instance.database.get_db_session()
        doctor_info = get_all_doctor_info(session)

        doctor_list = []
        for doctor in doctor_info:
            doctor_list.append(DoctorInfo(
                id=doctor.id,
                name=doctor.name,
                sex=doctor.sex,
                id_card=doctor.id_number,
                phone=doctor.phone,
                department=doctor.department,
                img_id=int(doctor.avatar_image),
                is_admin=doctor.is_admin,
                title=doctor.title
            ))
        return GetDoctorListRequest(info=doctor_list)

    async def GetDoctorInfoByName(self, request: DoctorName) -> GetDoctorListRequest:
        session = instance.database.get_db_session()
        doctor_info = get_doctor_info_by_name(request.name, session)
        doctor_list = []
        for doctor in doctor_info:
            doctor_list.append(DoctorInfo(
                id=doctor.id,
                name=doctor.name,
                sex=doctor.sex,
                id_card=doctor.id_number,
                phone=doctor.phone,
                department=doctor.department,
                img_id=int(doctor.avatar_image),
                is_admin=doctor.is_admin,
                title=doctor.title
            ))
        return GetDoctorListRequest(info=doctor_list)

    async def GetDoctorInfoById(self, request: DoctorId) -> DoctorInfo:
        session = instance.database.get_db_session()
        doctor = get_doctor_info_by_id(request.id, session)
        return DoctorInfo(
                id=doctor.id,
                name=doctor.name,
                sex=doctor.sex,
                id_card=doctor.id_number,
                phone=doctor.phone,
                department=doctor.department,
                img_id=int(doctor.avatar_image),
                is_admin=doctor.is_admin,
                title=doctor.title
            )


register_user_http_server(register_fastapi_route, DoctorServiceImpl(), parse_request, parse_reply)
