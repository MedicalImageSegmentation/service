from sqlalchemy import Column, BigInteger
from sqlalchemy.orm import declarative_base

from modles.base_model import BaseModel

base = declarative_base()


class DoctorPatientEntity(BaseModel, base):
    __tablename__ = 'doctor_patient'

    id = Column(BigInteger, primary_key=True, autoincrement=True, comment='id')
    doctor_id = Column(BigInteger, nullable=False, comment='医生id')
    patient_id = Column(BigInteger, nullable=False, comment='病人id')
