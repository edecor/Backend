to run locally, 

- install poetry, docker, 
- clone repo and create a folder named config in the root dir providing some configs. See [this](https://github.com/wemake-services/wemake-django-template/tree/master/%7B%7Bcookiecutter.project_name%7D%7D/config).
- run `docker-compose up --build`
- you need to run migrations for running the first time, the syntax will be `docker-compose exec web python manage.py [command] --settings=core.settings.local`.Furthermore, replace command with any stuff you need to run.
- contact me if you are lost