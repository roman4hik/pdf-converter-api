import mimetypes
from rest_framework import serializers

VALID_FILE_TYPES = ['text/html']


class HTMLConverterRequestSerializer(serializers.Serializer):

    link = serializers.CharField(required=False)
    file = serializers.FileField(required=False)

    def validate(self, attrs):
        data = super().validate(attrs)
        if not data.get('link') and not data.get('file'):
            raise serializers.ValidationError("You should send 'link' or 'file'")
        return data

    def validate_file(self, file):
        if file and mimetypes.guess_type(file.name)[0] not in VALID_FILE_TYPES:
            raise serializers.ValidationError("This is not valid files")
        return file