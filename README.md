To run locally, 

* install python, docker and poetry. Optionally postgresql(though not required 
because the existing setup uses a postgresql docker image).
* run ```docker-compose up --build``` for starting the whole process for the 
first time. But it will throw an error saying that no .env file is found. To fix 
it, go to config/.env.template file and follow the instructions. The default 
settings there are "ok" for starting.  
* After that, you need to go inside the containers(it is also possible to not get 
inside containers and but nevertheless run commands by running only ```docker exec [container name] command``` 
ie not passing the i and t flags which respectively mean interactive and allocate
a [tty](https://en.wikipedia.org/wiki/Tty_(Unix)). Learn more on
 [docker exec](https://docs.docker.com/engine/reference/commandline/exec/)) which will probably
be named something like "backend-[db/web]-1" which you can confirm by running 
```docker ps``` from a command line. To get inside and access the command line, run 
```docker exec -it [container name] bash``` which will take you to a bash prompt. 
* First you need to go inside the "web" container. Then run 
```python manage.py migrate```. It's possible that you encounter some errors. Come to me in that case.
After that, you can populate the empty database by running fixtures one by one
```python manage.py loaddata [name of fixture]```. 
* Now if you head over to "localhost:8000" or "127.0.0.1:8000", you should see a running site!
 