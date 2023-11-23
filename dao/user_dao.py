from sqlalchemy.orm import Session

from modles.doctor_entity import DoctorEntity


def verify_user_password(username, password: str, session: Session) -> DoctorEntity:
    doctor = session.query(DoctorEntity).filter(
        DoctorEntity.name == username,
        DoctorEntity.deleted == False
    ).first()

    if doctor and doctor.password == password:
        return doctor
    else:
        return None
