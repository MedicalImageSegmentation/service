from modles.base_model import BaseModel
from sqlalchemy import BigInteger, Column, String, Integer, Text
from sqlalchemy.orm import declarative_base

base = declarative_base()


class PatientEntity(BaseModel, base):
    __tablename__ = 'patient'

    id = Column(BigInteger, primary_key=True, autoincrement=True, comment='id')
    sex = Column(String(10), nullable=False, comment='性别')
    age = Column(Integer, nullable=True, comment='年龄')
    name = Column(String(64), nullable=False, comment='用户名')
    id_number = Column(String(20), nullable=False, comment='身份证')
    des = Column(Text, nullable=True, comment='医生备注')
    diagnosis_date = Column(String(50), nullable=True, comment='诊断时间')
    phone = Column(String(10), nullable=True, comment='电话号')
    department = Column(BigInteger, nullable=False, comment='所属科室')

    def __init__(self, sex, age, name, id_number, des, phone, department, date):
        self.sex = sex
        self.age = age
        self.name = name
        self.id_number = id_number
        self.des = des
        self.phone = phone
        self.department = department
        self.diagnosis_date = date
