from rest_framework import generics, permissions

from converter.serializers import HTMLConverterRequestSerializer
from converter.services import HTMLConverter, ResponseService


class HTMLConverterAPIView(generics.GenericAPIView):

    permission_classes = (permissions.AllowAny, )
    serializer_class = HTMLConverterRequestSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            bytes_file, file_name = HTMLConverter.convert(serializer.validated_data)
        except OSError:
            return ResponseService.bad_response()
        return ResponseService.response(bytes_file, file_name)
