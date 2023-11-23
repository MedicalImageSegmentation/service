from sqlalchemy.orm import Session

from modles.department import DepartmentEntity


def create_department(department_name: str, session: Session) -> DepartmentEntity:
    department = session.add(DepartmentEntity(name=department_name))
    session.commit()
    return department


def get_all_department_info(session: Session) -> list[DepartmentEntity]:
    return session.query(DepartmentEntity).all()
