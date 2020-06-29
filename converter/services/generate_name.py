
PDF_EXTENSION = 'pdf'
DEFAULT_NAME = 'converted.pdf'


class GenerateName:

    @staticmethod
    def change_extension(file_name: str):
        result = file_name.split('.')
        result[-1] = PDF_EXTENSION
        return '.'.join(result)

    @classmethod
    def generate(cls, file_name=None) -> str:
        if file_name:
            return cls.change_extension(file_name)
        return DEFAULT_NAME
