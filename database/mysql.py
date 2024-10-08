from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config.config import settings
from modles.base_model import CustomSession


class Database:

    def __init__(self) -> None:
        self.connection_is_active = False
        self.engine = None

    def get_db_connection(self):
        if not self.connection_is_active:
            connect_args = {"connect_timeout": int(settings.DATABASE_CONNECT_TIMEOUT)}
            try:
                self.engine = create_engine(settings.DATABASE_SOURCE,
                                            pool_size=int(settings.DATABASE_POOL_SIZE),
                                            pool_recycle=int(settings.DATABASE_POOL_RECYCLE),
                                            pool_timeout=int(settings.DATABASE_POOL_TIMEOUT),
                                            connect_args=connect_args)
                print("数据库连接成功")
                self.connection_is_active = True
            except Exception as e:
                print("Error connecting to MySQL DB:", e)
        return self.engine

    def get_db_session(self):
        if self.connection_is_active is False:
            self.get_db_connection()  # 确保数据库引擎已经被创建和配置
        try:
            session = sessionmaker(bind=self.engine, class_=CustomSession)
            return session()
        except Exception as e:
            print("Error getting DB session:", e)
            return None
