from fastapi import HTTPException

from api.medicalImagesegmentation.file import file_pb2 as api_dot_medicalImagesegmentation_dot_file_dot_file__pb2
from api.medicalImagesegmentation.file.file_pb2 import GetUploadUrlRequest, GetUploadReply, GetDownloadUrlRequest, \
    GetDownloadUrlReply, GetDownloadUrlByStrRequest, FileList, GetFileListByTypeRequest
from api.medicalImagesegmentation.file.file_pb2_http import FileServicer, register_file_http_server
from core.router_register import parse_request, parse_reply, register_fastapi_route, request_context
from dao.file_dao import verify_file_eTag, create_fileinfo, update_file_info, get_file_info_by_id, \
    get_file_info_by_name, get_file_info_by_tag, get_file_list_by_type
from core.app import instance
from modles.file_entity import FileEntity


class FileServiceImpl(FileServicer):
    async def GetUploadUrl(self, request: GetUploadUrlRequest) -> GetUploadReply:
        session = instance.database.get_db_session()
        file = verify_file_eTag(request.e_tag, session)

        if file is not None:
            if file.user_id is None:
                file.user_id = 0
                update_file_info(file, session)

            if file.is_Upload is False:
                url = instance.minio_client.get_minio_client().presigned_put_object('web', request.e_tag)
                return GetUploadReply(url=url, id=file.id)

            raise HTTPException(status_code=303)

        file_info = FileEntity()
        file_info.e_tag = request.e_tag
        file_info.file_name = request.file_name
        file_info.user_id = 0
        file_info.file_type = request.file_type
        file_info.is_Upload = False

        create_fileinfo(file_info, session)

        url = instance.minio_client.get_minio_client().presigned_put_object('web', request.e_tag)

        return GetUploadReply(id=file_info.id, url=url)

    async def GetDownloadUrlByid(self, request: GetDownloadUrlRequest) -> GetDownloadUrlReply:
        session = instance.database.get_db_session()
        file = get_file_info_by_id(request.id, session)
        if file is None:
            raise HTTPException(status_code=404, detail="file not found")

        url = instance.minio_client.get_minio_client().presigned_get_object('web', file.e_tag, response_headers={
            'response-content-disposition': f'attachment; filename="{file.file_name}"'})

        return GetDownloadUrlReply(url=url, file_name=file.file_name)

    async def GetDownloadUrlByFileName(self, request: GetDownloadUrlByStrRequest) -> GetDownloadUrlReply:
        session = instance.database.get_db_session()
        file = get_file_info_by_name(request.info, session)
        if file is None:
            raise HTTPException(status_code=404, detail="file not found")

        url = instance.minio_client.get_minio_client().presigned_get_object('web', file.e_tag, response_headers={
            'response-content-disposition': f'attachment; filename="{file.file_name}"'})

        return GetDownloadUrlReply(url=url, file_name=file.file_name)

    async def GetDownloadUrlByTag(self, request: GetDownloadUrlByStrRequest) -> GetDownloadUrlReply:
        session = instance.database.get_db_session()
        file = get_file_info_by_tag(request.info, session)
        if file is None:
            raise HTTPException(status_code=404, detail="file not found")

        url = instance.minio_client.get_minio_client().presigned_get_object('web', file.e_tag, response_headers={
            'response-content-disposition': f'attachment; filename="{file.file_name}"'})

        return GetDownloadUrlReply(url=url, file_name=file.file_name)

    async def GetFileListByType(self, request: GetFileListByTypeRequest) -> FileList:
        session = instance.database.get_db_session()
        file_info = get_file_list_by_type(request.type, session)

        file_list = []
        for file in file_info:
            file_list.append(GetUploadUrlRequest(
                file_name=file.file_name,
                file_size=100,
                e_tag=file.e_tag,
                file_type=file.file_type
            ))
        return FileList(info=file_list)


register_file_http_server(register_fastapi_route, FileServiceImpl(), parse_request, parse_reply)
