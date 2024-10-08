from sqlalchemy import Column, BigInteger, String, Boolean
from sqlalchemy.orm import declarative_base

from modles.base_model import BaseModel

base = declarative_base()


class DoctorEntity(BaseModel, base):
    __tablename__ = 'doctor'

    id = Column(BigInteger, primary_key=True, autoincrement=True, comment='id')
    sex = Column(String(10), nullable=False, comment='性别')
    name = Column(String(64), nullable=False, comment='用户名')
    avatar_image = Column(String(500), nullable=True, comment='用户头像')
    password = Column(String(50), nullable=False, comment='密码')
    is_admin = Column(Boolean, nullable=False, default=False, comment='是否为系主任')
    id_number = Column(String(20), nullable=False, comment='身份证')
    phone = Column(String(10), nullable=True, comment='电话号')
    department = Column(BigInteger, nullable=False, comment='所属科室')
    title = Column(String(10), nullable=True, comment='医生职称')

    def __init__(self, sex=None, name=None, avatar_image=None, password=None, is_admin=None, id_number=None, phone=None,
                 department=None, title=None):
        self.sex = sex
        self.name = name
        self.avatar_image = avatar_image
        self.password = password
        self.is_admin = is_admin
        self.id_number = id_number
        self.phone = phone
        self.department = department
        self.title = title
