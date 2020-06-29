import pdfkit
from typing import Tuple

from .generate_name import GenerateName


class HTMLConverter:

    @staticmethod
    def _convert_from_link(link) -> Tuple[bytes, str]:
        pdf = pdfkit.from_url(link, False)
        return pdf, GenerateName.generate()

    @staticmethod
    def _converter_from_file(file) -> Tuple[bytes, str]:
        pdf = pdfkit.from_string(file.read().decode('utf-8'), False)
        return pdf, GenerateName.generate(file.name)

    @classmethod
    def convert(cls, data):
        if 'file' in data:
            return cls._converter_from_file(data['file'])
        return cls._convert_from_link(data['link'])
