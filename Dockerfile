FROM rcarmo/ubuntu-python:onbuild

LABEL maintainer="roman4hik"

ARG DATABASE_URL
ENV PYTHONUNBUFFERED 1
ENV PROJECT_PATH ${PROJECT_PATH:-/code}
RUN mkdir ${PROJECT_PATH}
WORKDIR ${PROJECT_PATH}
COPY . ${PROJECT_PATH}/
ENV DATABASE_URL ${DATABASE_URL:-postgres://myprojectuser:password@converter-db:5432/test_converter}
ENV LANG C.UTF-8
ENV LANGUAGE C.UTF-8
ENV LC_ALL C.UTF-8

# install wkhtmltopdf
RUN apt update && apt -y install wget \
    && wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.bionic_amd64.deb \
    && apt install -y ./wkhtmltox_0.12.5-1.bionic_amd64.deb

# install pipenv
RUN pip install --no-cache-dir pipenv \
    && pipenv install --system --deploy \
    && chmod +x ${PROJECT_PATH}/entrypoint_api.sh

EXPOSE 8000

ENTRYPOINT ${PROJECT_PATH}/entrypoint_api.sh
