from django.http import StreamingHttpResponse
from django.core.files.base import ContentFile

from rest_framework import response, status


CONVERT_ERROR_MESSAGE = 'We can not convert it'


class ResponseService:

    @staticmethod
    def response(bytes_file: bytes, file_name: str):
        file = ContentFile(bytes_file)
        resp = StreamingHttpResponse(file, content_type='application/pdf')
        resp['Content-Length'] = file.size
        resp['Content-Disposition'] = 'attachment; filename="%s"' % file_name
        return resp

    @staticmethod
    def bad_response():
        return response.Response({'message': CONVERT_ERROR_MESSAGE}, status=status.HTTP_400_BAD_REQUEST)
