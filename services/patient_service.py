from google.protobuf.empty_pb2 import Empty

from api.medicalImagesegmentation.patient.patient_pb2 import PatientInfo, PatientId, GetPatientListRequest
from api.medicalImagesegmentation.patient.patient_pb2_http import PatientServicer, register_patient_http_server
from core.app import instance
from core.router_register import register_fastapi_route, parse_request, parse_reply
from dao.patient_dao import create_patient_info, add_patient_doctor_info, modify_patient_info, get_patient_info_by_id, \
    get_all_patient, get_patient_to_doctor_id
from modles.patient_entity import PatientEntity


class PatientServiceImpl(PatientServicer):
    async def AddPatientInfo(self, request: PatientInfo) -> PatientId:
        session = instance.database.get_db_session()
        patient = create_patient_info(PatientEntity(
            name=request.name,
            age=request.age,
            sex=request.sex,
            id_number=request.id_card,
            department=request.department,
            des=request.des,
            phone=request.phone,
            date=request.diagnosis_date
        ), session)
        add_patient_doctor_info(patient_id=patient.id, doctor_id=request.doctor, session=session)

        return PatientId(id=patient.id)

    async def ModifyPatientInfo(self, request: PatientInfo) -> PatientId:
        session = instance.database.get_db_session()
        patient = get_patient_info_by_id(request.id, session)
        patient.name = request.name
        patient.age = request.age
        patient.sex = request.sex
        patient.id_number = request.id_card
        patient.department = request.department
        patient.des = request.des
        patient.phone = request.phone
        patient.date = request.diagnosis_date
        modify_patient_info(patient, session)
        return PatientId(id=patient.id)

    async def GetPatientList(self, request: Empty) -> GetPatientListRequest:
        session = instance.database.get_db_session()
        patient_info = get_all_patient(session)

        patient_list = []
        for patient in patient_info:
            doctor_id = get_patient_to_doctor_id(patient.id, session)
            patient_list.append(PatientInfo(
                id=patient.id,
                name=patient.name,
                age=patient.age,
                sex=patient.sex,
                id_card=patient.id_number,
                doctor=doctor_id,
                phone=patient.phone,
                des=patient.des,
                diagnosis_date=patient.diagnosis_date
            ))
        return GetPatientListRequest(info=patient_list)


register_patient_http_server(register_fastapi_route, PatientServiceImpl(), parse_request, parse_reply)