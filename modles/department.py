from sqlalchemy import Column, BigInteger, String, Boolean
from sqlalchemy.orm import declarative_base

from modles.base_model import BaseModel

base = declarative_base()


class DepartmentEntity(BaseModel, base):
    __tablename__ = 'department'

    id = Column(BigInteger, primary_key=True, autoincrement=True, comment='id')
    name = Column(String(20), nullable=False, comment='科室名称')
