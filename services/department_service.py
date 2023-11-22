
from google.protobuf.empty_pb2 import Empty

from api.medicalImagesegmentation.department.department_pb2 import DepartmentInfo, DepartmentId, DepartmentInfoList
from api.medicalImagesegmentation.department.department_pb2_http import DepartmentServicer


class DepartmentServiceImpl(DepartmentServicer):
    async def AddDepartmentInfo(self, request: DepartmentInfo) -> DepartmentId:
        pass

    async def GetDepartmentInfo(self, request: Empty) -> DepartmentInfoList:
        pass