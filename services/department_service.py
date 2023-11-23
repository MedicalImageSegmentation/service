from fastapi import HTTPException
from google.protobuf.empty_pb2 import Empty

from api.medicalImagesegmentation.department.department_pb2 import DepartmentInfo, DepartmentId, DepartmentInfoList
from api.medicalImagesegmentation.department.department_pb2_http import DepartmentServicer, \
    register_department_http_server
from core.app import instance
from core.router_register import request_context, register_fastapi_route, parse_request, parse_reply
from dao.department_dao import create_department, get_all_department_info
from dao.user_dao import verify_user_is_admin


class DepartmentServiceImpl(DepartmentServicer):
    async def AddDepartmentInfo(self, request: DepartmentInfo) -> DepartmentId:
        session = instance.database.get_db_session()
        is_admin = verify_user_is_admin(request_context.get().userid, session)
        if is_admin is False:
            raise HTTPException(status_code=403, detail="Forbidden")

        department = create_department(request.name, session)

        return DepartmentId(id=department.id)

    async def GetDepartmentInfo(self, request: Empty) -> DepartmentInfoList:
        session = instance.database.get_db_session()
        department_info = get_all_department_info(session)
        department_list = []
        for dep in department_info:
            department_list.append(DepartmentInfo(id=dep.id, name=dep.name))

        return DepartmentInfoList(info=department_list)


register_department_http_server(register_fastapi_route, DepartmentServiceImpl(), parse_request, parse_reply)
