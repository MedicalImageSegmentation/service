from pydantic import BaseModel
from sqlalchemy import BigInteger, Column, String, Text, Integer
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
    phone = Column(String(10), nullable=True, comment='电话号')
    department = Column(BigInteger, nullable=False, comment='所属科室')
