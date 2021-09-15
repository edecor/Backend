FROM python:3.9-slim-buster

ARG DJANGO_ENV

ENV DJANGO_ENV=${DJANGO_ENV} \
    PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONDONTWRITEBYTECODE=1 \
    DOCKERIZE_VERSION=v0.6.1 \
    PATH="$PATH:/root/.local/bin" 

RUN apt-get update && apt-get upgrade -y \
    && apt-get install --no-install-recommends -y \
    bash \
    wget \
    curl \
    libmagic-dev \
    && curl -sSL 'https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py' | python - \
    && wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    # Cleaning cache:
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && apt-get clean -y && rm -rf /var/lib/apt/lists/

WORKDIR /code 

COPY ./entrypoint.sh /docker-entrypoint.sh

COPY ./poetry.lock ./pyproject.toml /code/

RUN poetry config virtualenvs.create false \
    && poetry install \
    $(if [ "$DJANGO_ENV" = 'production' ]; then echo '--no-dev'; fi) \
    --no-interaction --no-ansi \
    && if [ "$DJANGO_ENV" = 'production' ]; then rm -rf "$POETRY_CACHE_DIR"; fi \
    && mkdir -p /var/www/django/static /var/www/django/media 

# test for production, 
COPY . /code

ENTRYPOINT ["/docker-entrypoint.sh" ]
