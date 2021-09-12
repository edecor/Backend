FROM python:3.9-slim-buster

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONDONTWRITEBYTECODE=1 \
    DOCKERIZE_VERSION=v0.6.1 \
    # POETRY_VERSION=1.1.8 \
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

RUN chmod +x '/docker-entrypoint.sh' \
    && groupadd -r web && useradd -d /code -r -g web web \
    && chown web:web -R /code \
    && mkdir -p /var/www/django/static /var/www/django/media \
    && chown web:web /var/www/django/static /var/www/django/media

COPY --chown=web:web ./poetry.lock ./pyproject.toml /code/

RUN poetry config virtualenvs.create false \
    && poetry install --no-ansi

USER web 

ENTRYPOINT ["/docker-entrypoint.sh" ]