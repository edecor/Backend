#!/usr/bin/env sh

set -o errexit
set -o nounset

# We are using `gunicorn` for production, see:
# http://docs.gunicorn.org/en/stable/configure.html

# Check that $DJANGO_ENV is set to "production",
# fail otherwise, since it may break things:

if [ "$DJANGO_ENV" != 'production' ]; then
  echo 'Error: DJANGO_ENV is not set to "production".'
  echo 'Application will not start.'
  exit 1
fi

export DJANGO_SETTINGS_MODULE=core.settings.production
mkdir -p /var/log/gunicorn
touch /var/log/gunicorn/access.log /var/log/gunicorn/error.log

# Run python specific scripts:
# Running migrations in startup script might not be the best option, see:
# docs/pages/template/production-checklist.rst
# python /code/manage.py migrate --noinput
# python /code/manage.py collectstatic --noinput
# python /code/manage.py compilemessages

# Start gunicorn:
# Docs: http://docs.gunicorn.org/en/stable/settings.html
# Concerning `workers` setting see:
# https://github.com/wemake-services/wemake-django-template/issues/1022

gunicorn core.wsgi -c /code/config/gunicorn.conf.py