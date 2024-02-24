FROM python:3.11

RUN apt-get update && apt-get install -y
RUN apt-get install chromium vim -y

WORKDIR /usr/src/app

ARG GIT_COMMIT_SHA
ARG GIT_COMMIT_SHORT_SHA
ARG PIP_EXTRA_INDEX_URL
ARG STAGE

# Declare container user variables
ARG CONTAINER_USER_NAME=yocoreseller

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV GIT_COMMIT_SHA=${GIT_COMMIT_SHA}
ENV GIT_COMMIT_SHORT_SHA=${GIT_COMMIT_SHORT_SHA}
ENV STAGE=${STAGE}
ENV PIP_EXTRA_INDEX_URL=${PIP_EXTRA_INDEX_URL}

RUN pip install pip-tools

COPY . /usr/src/app/

RUN set -x \
    # create yocoreseller user/group first, to be consistent throughout docker variants
    && addgroup --system ${CONTAINER_USER_NAME} || true \
    && adduser --system --disabled-login --ingroup ${CONTAINER_USER_NAME} --home /home/${CONTAINER_USER_NAME} --gecos "${CONTAINER_USER_NAME} user" --shell /bin/false  ${CONTAINER_USER_NAME} || true

RUN if [ "$STAGE" = "dev" -o "$STAGE" = "local" ]; \
    then pip-sync --extra-index-url $PIP_EXTRA_INDEX_URL requirements.txt dev-requirements.txt --pip-args "--no-cache-dir"; \
    else pip-sync --extra-index-url $PIP_EXTRA_INDEX_URL requirements.txt --pip-args "--no-cache-dir"; \
    fi


RUN python /usr/src/app/src/manage.py collectstatic --no-input

USER $CONTAINER_USER_NAME

CMD [ "python", "src/manage.py", "runserver", "0.0.0.0:8000" ]
