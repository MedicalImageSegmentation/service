CREATE TABLE doctor_patient
(
    id              BIGINT(20)  PRIMARY KEY AUTO_INCREMENT      COMMENT 'id',
    doctor_id       BIGINT                  NOT NULL            COMMENT '医生id',
    patient_id      BIGINT                  NOT NULL            COMMENT '病人id',
    ctime           DATETIME                NULL                COMMENT '创建时间',
    mtime           DATETIME                NULL                COMMENT '修改时间',
    deleted         BOOLEAN DEFAULT FALSE   NOT NULL            COMMENT '是否删除'
)