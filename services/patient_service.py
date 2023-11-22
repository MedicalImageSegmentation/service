
from google.protobuf.empty_pb2 import Empty

from api.medicalImagesegmentation.patient.patient_pb2 import PatientInfo, PatientId, GetPatientListRequest
from api.medicalImagesegmentation.patient.patient_pb2_http import PatientServicer


class PatientServiceImpl(PatientServicer):
    async def AddPatientInfo(self, request: PatientInfo) -> PatientId:
        pass

    async def ModifyPatientInfo(self, request: PatientInfo) -> PatientId:
        pass

    async def GetPatientList(self, request: Empty) -> GetPatientListRequest:
        pass