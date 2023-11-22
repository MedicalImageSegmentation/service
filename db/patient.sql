CREATE TABLE patient
(
    id              BIGINT(20)  PRIMARY KEY AUTO_INCREMENT      COMMENT 'id',
    sex             VARCHAR(10)             NOT NULL            COMMENT '性别',
    age             INT                     NULL                COMMENT '年龄',
    name            VARCHAR(64)             NOT NULL            COMMENT '用户名',
    id_number       VARCHAR(20)             NOT NULL            COMMENT '身份证',
    des             TEXT                    NULL                COMMENT '医生备注',
    phone           VARCHAR(10)             NULL                COMMENT '电话号',
    department      BIGINT(20)              NOT NULL            COMMENT '所属科室',
    ctime           DATETIME                NULL                COMMENT '创建时间',
    mtime           DATETIME                NULL                COMMENT '修改时间',
    deleted         BOOLEAN DEFAULT FALSE   NOT NULL            COMMENT '是否删除'
)