from sqlalchemy.orm import Session

from modles.doctor_patient_entity import DoctorPatientEntity
from modles.patient_entity import PatientEntity


def create_patient_info(patient: PatientEntity, session: Session) -> PatientEntity:
    session.add(patient)
    session.commit()
    return patient


def add_patient_doctor_info(patient_id, doctor_id: int, session: Session):
    session.add(DoctorPatientEntity(patient_id=patient_id, doctor_id=doctor_id))
    session.commit()


def modify_patient_info(patient: PatientEntity, session: Session) -> PatientEntity:
    session.merge(patient)
    session.commit()
    return patient


def get_patient_info_by_id(patient_id: int, session: Session) -> PatientEntity:
    return session.query(PatientEntity).filter(PatientEntity.id == patient_id).first()


def get_all_patient(session: Session) -> list[PatientEntity]:
    return session.query(PatientEntity).all()


def get_patient_to_doctor_id(patient: int, session: Session) -> int:
    doctor = session.query(DoctorPatientEntity).filter(DoctorPatientEntity.patient_id == patient).one()
    return doctor.doctor_id
