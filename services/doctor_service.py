from queue import Empty

from api.medicalImagesegmentation.user.user_pb2 import LoginRequest, DoctorInfo, DoctorId, GetDoctorListRequest, \
    DoctorName
from api.medicalImagesegmentation.user.user_pb2_http import UserServicer


class DoctorServiceImpl(UserServicer):
    async def Login(self, request: LoginRequest) -> Empty:
        pass

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