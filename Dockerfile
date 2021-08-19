# # FROM python:3.9

# # ENV PYTHONFAULTHANDLER=1 \
# #     PYTHONHASHSEED=random \
# #     PYTHONDONTWRITEBYTECODE=1 \
# #     PYTHONUNBUFFERED=1 \
# #     # poetry:
# #     POETRY_NO_INTERACTION=1 \
# #     POETRY_VIRTUALENVS_CREATE=false \
# #     PATH="/root/.local/bin:$PATH"

# # RUN apt-get update && apt-get upgrade -y \
# #     && apt-get install --no-install-recommends -y \
# #     curl \
# #     # Installing `poetry` package manager:
# #     # https://github.com/python-poetry/poetry
# #     && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python - 

# # # Set work directory
# # WORKDIR /code

# # COPY ./poetry.lock ./pyproject.toml /code/

# # RUN poetry config virtualenvs.create false \
# #     && poetry install 

# # # Copy project
# # COPY . /code/
# FROM python:3.9


# ENV PYTHONFAULTHANDLER=1 \
#     PYTHONUNBUFFERED=1 \
#     PYTHONHASHSEED=random \
#     PIP_NO_CACHE_DIR=off \
#     PIP_DISABLE_PIP_VERSION_CHECK=on \
#     PIP_DEFAULT_TIMEOUT=100 \
#     POETRY_VERSION=1.1.7

# # System deps:
# RUN pip install "poetry==$POETRY_VERSION"

# # Copy only requirements to cache them in docker layer
# WORKDIR /code
# COPY ./poetry.lock ./pyproject.toml /code/

# # Project initialization:
# RUN poetry config virtualenvs.create false \
#     && poetry install 

# # Creating folders, and files for a project:
# COPY . /code







# This Dockerfile uses multi-stage build to customize DEV and PROD images:
# https://docs.docker.com/develop/develop-images/multistage-build/

FROM python:3.9



ENV BUILD_ONLY_PACKAGES='wget' \
    # python:
    PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONDONTWRITEBYTECODE=1 \
    # pip:
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # dockerize:
    DOCKERIZE_VERSION=v0.6.1 \
    # tini:
    TINI_VERSION=v0.19.0 \
    # poetry:
    POETRY_VERSION=1.1.7 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    PATH="$PATH:/root/.poetry/bin"


# System deps:
RUN apt-get update && apt-get upgrade -y \
    && apt-get install --no-install-recommends -y \
    bash \
    build-essential \
    curl \
    gettext \
    git \
    libpq-dev \
    # Defining build-time-only dependencies:
    $BUILD_ONLY_PACKAGES \
    # Installing `dockerize` utility:
    # https://github.com/jwilder/dockerize
    && wget "https://github.com/jwilder/dockerize/releases/download/${DOCKERIZE_VERSION}/dockerize-linux-amd64-${DOCKERIZE_VERSION}.tar.gz" \
    && tar -C /usr/local/bin -xzvf "dockerize-linux-amd64-${DOCKERIZE_VERSION}.tar.gz" \
    && rm "dockerize-linux-amd64-${DOCKERIZE_VERSION}.tar.gz" && dockerize --version \
    # Installing `tini` utility:
    # https://github.com/krallin/tini
    && wget -O /usr/local/bin/tini "https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini" \
    && chmod +x /usr/local/bin/tini && tini --version \
    # Installing `poetry` package manager:
    # https://github.com/python-poetry/poetry
    && curl -sSL 'https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py' | python \
    && poetry --version \
    # Removing build-time-only dependencies:
    && apt-get remove -y $BUILD_ONLY_PACKAGES \
    # Cleaning cache:
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && apt-get clean -y && rm -rf /var/lib/apt/lists/*

WORKDIR /code

# This is a special case. We need to run this script as an entry point:
COPY ./entrypoint.sh /docker-entrypoint.sh

# Setting up proper permissions:
RUN chmod +x '/docker-entrypoint.sh' \
    && groupadd -r web && useradd -d /code -r -g web web \
    && chown web:web -R /code \
    && mkdir -p /var/www/django/static /var/www/django/media \
    && chown web:web /var/www/django/static /var/www/django/media

# Copy only requirements, to cache them in docker layer
COPY --chown=web:web ./poetry.lock ./pyproject.toml /code/

# Project initialization:
RUN poetry version \
    && poetry install \
    --no-interaction --no-ansi \
    # Upgrading pip, it is insecure, remove after `pip@21.1`
    && poetry run pip install -U pip 
# Cleaning poetry installation's cache for production:

# Running as non-root user:
# USER web

# We customize how our app is loaded with the custom entrypoint:
ENTRYPOINT ["tini", "--", "/docker-entrypoint.sh"]


# # The following stage is only for Prod:
# # https://wemake-django-template.readthedocs.io/en/latest/pages/template/production.html
# FROM development_build AS production_build
# COPY --chown=web:web . /code