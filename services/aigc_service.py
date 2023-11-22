from google.protobuf.empty_pb2 import Empty


from api.medicalImagesegmentation.aigc.aigc_pb2 import FileHash
from api.medicalImagesegmentation.aigc.aigc_pb2_http import AigcServicer


class AigcService(AigcServicer):
    async def ModelHandle(self, request: FileHash) -> Empty:
        pass
