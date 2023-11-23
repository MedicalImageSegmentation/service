from sqlalchemy.orm import Session

from modles.doctor_entity import DoctorEntity


def verify_user_is_admin(user_id: int, session: Session) -> bool:
    user_info = session.query(DoctorEntity).filter(DoctorEntity.id == user_id, DoctorEntity.is_admin == True,
                                                   DoctorEntity.deleted == False).first()

    if user_info is None:
        return False
    return True


def verify_user_password(username, password: str, session: Session) -> DoctorEntity:
    doctor = session.query(DoctorEntity).filter(
        DoctorEntity.name == username,
        DoctorEntity.deleted == False
    ).first()

    if doctor and doctor.password == password:
        return doctor
    else:
        return None


def create_doctor_info(doctor: DoctorEntity, session: Session) -> DoctorEntity:
    session.add(doctor)
    session.commit()
    return doctor


def modify_doctor_info(doctor: DoctorEntity, session: Session) -> DoctorEntity:
    session.merge(doctor)
    session.commit()
    return doctor


def get_all_doctor_info(session: Session) -> list[DoctorEntity]:
    return session.query(DoctorEntity).all()


def get_doctor_info_by_name(name: str, session: Session) -> list[DoctorEntity]:
    return session.query(DoctorEntity).filter(DoctorEntity.name.like(f'%{name}%'))


def get_doctor_info_by_id(id: int, session: Session) -> DoctorEntity:
    return session.query(DoctorEntity).filter(DoctorEntity.id == id).one()
