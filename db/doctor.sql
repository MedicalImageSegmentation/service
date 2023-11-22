CREATE TABLE doctor
(
    id              BIGINT(20)  PRIMARY KEY AUTO_INCREMENT      COMMENT 'id',
    sex             VARCHAR(10)             NOT NULL            COMMENT '性别',
    name            VARCHAR(64)             NOT NULL            COMMENT '用户名',
    avatar_image    VARCHAR(500)            NULL                COMMENT '用户头像',
    password        VARCHAR(50)             NOT NULL            COMMENT '密码',
    is_admin        BOOLEAN DEFAULT FALSE   NOT NULL            COMMENT '是否为系主任',
    id_number       VARCHAR(20)             NOT NULL            COMMENT '身份证',
    phone           VARCHAR(10)             NULL                COMMENT '电话号',
    department      BIGINT(20)              NOT NULL            COMMENT '所属科室',
    title           VARCHAR(10)             NULL                COMMENT '医生职称',
    ctime           DATETIME                NULL                COMMENT '创建时间',
    mtime           DATETIME                NULL                COMMENT '修改时间',
    deleted         BOOLEAN DEFAULT FALSE   NOT NULL            COMMENT '是否删除'
)