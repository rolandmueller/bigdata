# Docker Basics

## Install and Login

* Install docker
* Create a Login at Docker Hub
* Start your Docker Program on your computer
* Login in Docker locally
* In the command line

```bash
docker login
```

## Create a folder

Create a folder for the experiments and change into the folder:
```bash
mkdir docker
cd docker
```

## Check if Docker is running

Check if docker is installed. Enter in the command line (or power shell):

```bash
docker --version
```

Test docker:
```bash
docker run hello-world
```

More info about your Docker:
```bash
docker info
```

## Pulling an Image from Docker Hub

* Go to http://hub.docker.com/
* login
* search for Ubuntu
* What is the last version of Ubuntu?

So let us pull it from Dock Hub to your computer.

On you command line:
```bash
docker pull ubuntu
```

## List all Images

```bash
docker image ls
```

## List all Container

List all running containers:
```bash
docker container ls
```

List all containers:
```bash
docker container ls -a
```

## Running, stoping, and Attaching an Image

Starts Docker container and ends it right away:
```bash
docker run ubuntu
```

If you check the running containers, you see that there is no running container:
```bash
docker container ls
```

Starts Docker container and executes echo command:
```bash
docker run ubuntu echo "Hello BIPM"
```

Starts a Docker container and an interactive Bash. `-it` is short for `--interactive --tty` and will run it in the interactive mode:
```bash
docker run -it ubuntu bash
```

Some images have as a command line not Bash but a normal Shell `sh`. Normally you can always get the command line of a container.

You are now in the container and can interactively run commands:
```bash
pwd
```
```bash
ls
```
```bash
cd ~
```
```bash
ls
```
```bash
touch iwashere.txt
```
```bash
ls
```
To log out of the container, enter
```bash
exit
```

Now again the container is stopped.

If we login again,
```bash
docker run -it ubuntu bash
```
and go to your home directory
```bash
cd ~
```
check if the data is still there:
```bash
ls
```
The file is gone!

Check all containers.
```bash
docker container ls -a
```
```bash
CONTAINER ID        IMAGE                              COMMAND                  CREATED              STATUS                          PORTS               NAMES
a4cf0a5f41e7        ubuntu                             "bash"                   About a minute ago   Exited (0) 5 seconds ago                            objective_yonath
94cb0399ba60        ubuntu                             "bash"                   2 minutes ago        Exited (0) About a minute ago                       angry_goldstine
22863f7d24c0        ubuntu                             "bash"                   3 minutes ago        Exited (0) 3 minutes ago                            condescending_elgamal
```

The most right columnn you find `NAMES`. These names are automatically created. If we use the parameter `--name` we can name the container also by yourselfs.
You can also use the `CONTAINER ID` (first column) to identify a container  (e.g. a4cf0a5f41e7). There you do not have to write out the whole container ID but only use as many digits that are needed for identifying the container (normally two digits are sufficient)

Look not for the last but the the second last container (in this example `angry_goldstine` as NAME or `94cb0399ba60` as CONTAINER ID)

Restart the container (change the name or use the CONTAINER ID)
```bash
docker start angry_goldstine
```

Alternatively you could also use the CONTAINER ID (94cb0399ba60 in my case).
```bash
docker start 94cb0399ba60
```

You can als just use the first numbers of the CONATINER ID as long as they identify the container.
```bash
docker start 94
```

Login to an already running container with `docker exec` (change the CONTAINER ID);
```bash
docker exec -it 94 bash
```

`Ctrl+p` + `Ctrl+q` will turn the  interactive mode into a detached background (daemon) mode. That means you log out without stopping the container.

Check if the container is still running:
```bash
docker container ls
```

Login again. Alternatively to `docker exec -it` you can also use (change the CONTAINER ID)
```bash
docker attach 94
```

Go to your home directory
```bash
cd ~
```
check if the data is still there:
```bash
ls
```

The file is still here!

Use `Ctrl+p` + `Ctrl+q` to logout without stopping the container,

Check if the container is still running:
```bash
docker container ls
```

Stop the container if it is stil running (change 94cb0399ba60 to your container ID)
```bash
docker container stop 94cb0399ba60
```

Check if the container is still running:
```bash
docker container ls
```

## Deleting Containers

Check all containers:
```bash
docker container ls -a
```
Containers that you do not need anymore can be delete. This will delete all data on the container (change 94cb0399ba60 to your container ID)
```bash
docker container rm 94cb0399ba60
```

Check all containers:
```bash
docker container ls -a
```

You can delete all containers with
```bash
docker container prune
```
This is a dangerous command :-).

```bash
docker container ls -a
```
Everything gone.

## Containers and images

Let us start three different containers from the same iamge.
```bash
docker run -it -d --name ubuntu1 ubuntu bash
```
```bash
docker run -it -d --name ubuntu2 ubuntu bash
```
```bash
docker run -it -d --name ubuntu3 ubuntu bash
```

Meaning of the parameters:
* `--name` gives a container a name (e.g. ubuntu1)
* `-d` Detach: detaches the command line from the container so it is running in the background.


Check if all three containers running:
```bash
docker container ls
```

Start three more terminals, so that in total you have four terminals open.

In the second terminal, Enter
```bash
docker attach ubuntu1
```
In the third terminal, Enter
```bash
docker attach ubuntu2
```
In the fourth terminal, Enter
```bash
docker attach ubuntu3
```
In the termina of container ubuntu1 create a folder
```bash
mkdir iwashere
```
and check if it is there:
```bash
ls
```

In the termina of container ubuntu2 check if the folder `iwashere` is there:
```bash
ls
```

That means all containers are isolated.

Stop in the first terminal the ubuntu1 container.
```bash
docker container stop ubuntu1
```
What happens with your second terminal (where you are logged into ubuntu1)?

Stop all other containers.

# Define and build a new Image

Create a file with the name `Dockerfile` with the following content:

```bash
# Use an official Python runtime as a parent image
FROM python:3.7-slim

# Set the working directory to /app
WORKDIR /app

# Copy the app directory contents into the container at /app
COPY app/ /app

# Run computation.py when the container launches
CMD ["python", "computation.py"]
```


Create the `app` folder in change into the folder
```bash
mkdir app
```

Create the `computation.py` file in the `app` folder:
```python
my_list = [i**2 for i in range(10)]

print(my_list)
```


## Build a new Image

Run this command in the folder where the Dockerfile is:
```bash
docker build -t bipm_compute .
```
You can see the built bipm_compute image with:
```bash
docker image ls
```

# Run a Docker containers

To run the an image, use the following command:
```bash
docker run bipm_compute
```
This will initiate a new container, run it, and then after the process is finished, stop the container again.

The output should be:
```bash
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

You can see all running containers with
```bash
docker container ls
```
Because the container immediately stopped, you can not see the bipm_compute container.

However, with
```bash
docker container ls -a
```
you can also see the stopped containers.

## Volumes

Change the `computation.py` file to

```python
my_list = [i**3 for i in range(15)]

print(my_list)
```

If you run now again:
```bash
docker run bipm_compute
```
you get still the old output
```bash
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

You need to build again the image to reflect the change.
```bash
docker build -t bipm_compute .
```
Then after
```bash
docker run bipm_compute
```
you get
```bash
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
```

To more easily attach data to an image but also store resulting data (e.g. from a computation or from a database) independent of the lifetime of the image, we can use images.

We can mount an volume when you run a volume with the `-v` parameter. However, only absolute paths are possible. So first check out our current path with `pwd` (print working directory)
```bash
pwd
```
In my case, it is `/Users/rolandmueller/Documents/sourcecode/bigdata/docker`

Adjust the command for your path:
```bash
docker run -v /Users/rolandmueller/Documents/sourcecode/bigdata/docker/app/:/app bipm_compute
```

The `-v` flag expects two directories before and after the `:`. On the left of the `:` is the absolute path to a directory on the host system (your laptop) that will be mounted to an directory in the container (right side of `:`)

There is also a clumbsy always to use the relative path. This depends if you use Mac/Linux or Windows:

On Mac/Linux (includes the current path via \`pwd\`):
```bash
docker run -v `pwd`/app/:/app bipm_compute
```
Only on Windows (includes the current path via %CD%):
```bash
docker run -v %CD%/app/:/app bipm_compute
```

Change the `computation.py` file to

```python
my_list = [i**4 for i in range(5)]

print(my_list)
```

Run (Adjust the command for your path or use a realtive path):
```bash
docker run -v /Users/rolandmueller/Documents/sourcecode/bigdata/docker/app/:/app bipm_compute
```
You should see the new result with building the container again.

# Named Volumes

You can also create a volume directly with docker.

```bash
docker volume create bipm
```

This creates a volume on your computer that you can mount to a container.

List all existing volumes:
```bash
docker volume ls
```

Inspect a volume:
```bash
docker volume inspect bipm
```

Start container with the created volume and log into the contaienr:
```bash
docker run -it -v bipm:/bipm ubuntu bash
```

List:
```bash
ls
```
Change in the bipm folder (this is the mounted volume):
```bash
cd bipm
```

Create a file in this folder (this will be in the mounted volume):
```bash
touch iwashere.txt
```

The file is here:
```bash
ls
```

Exit the container:
```bash
exit
```

* List all containers
* Delete the last created container

Start a new container with the  volume and log into the container:
```bash
docker run -it -v bipm:/bipm ubuntu bash
```
Inside the container:
```bash
cd bipm
```
```bash
ls
```
The file is still there!


# Create a small Flask Web App

Based on https://docs.docker.com/compose/gettingstarted/

We will build a web application with `Flask` (http://flask.pocoo.org/). Create a `requirements.txt` file in the `app` folder. Here we can specify all python `pip` packages that we need:
```bash
Flask
```

Create the `app.py` file in the `app` folder:
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello BIPM!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
```

This mini Flask app creates a dynamic web applications:
*  `app = Flask(__name__)`: Creates the Flask object `app` that represent the main application
* @app.route('/'): This is a Python decorator. Python decorators (starting with `@`) are functions that change the behavior of other functions (https://realpython.com/primer-on-python-decorators/). Python decorators are  useful for example for logging or monitoring a function or calling a function via a web interface. Here we specify the web routing, that means what URL-path should call what function. Here we want, that the root URL (e.g. http://localhost/) should call the hello function. We could also link the function to any other URL-path like "/hello" so that the URL would be e.g. http://localhost/hello.
* `if __name__ == "__main__":` If we call a Python file with e.g. `python app.py`, the Python interpreter will assign the string `"__main__"` to the variable `__name__`. That means that this if statement will only be executed if it is run directly (and not if Python code is e.g. loaded as a module in another code).
* `app.run(host="0.0.0.0", port=80, debug=True)`: The Flask server starts and listens to port 80 and the debug mode is turned on.

Change the `Dockerfile` file:
```bash
# Use an official Python runtime as a parent image
FROM python:3.7-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY app/ /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["python", "app.py"]
```

Build the container:
```bash
docker build --tag=bipm_hello .
```

Run the container:
```bash
docker run -p 4000:80 bipm_hello
```

Meaning of the parameter:
* `-p` Publish Port: Publish your machine’s port 4000 to the container’s published port 80

Open in your browser http://localhost:4000/

Stop it with Control-C

Running it with detached mode:
```bash
docker run -d -p 4000:80 bipm_hello
```

The container is still running:
```bash
docker container ls
```

You see the list of running containers with the CONTAINER ID:
```bash
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS                  NAMES
ccf9e14d3f3a        bipm_hello       "python app.py"     40 seconds ago      Up 39 seconds       0.0.0.0:4000->80/tcp   modest_joliot
```

With the container ID you can stop the running container:
```bash
docker container stop ccf9e14d3f3a
```

Check if the container is still running:
```bash
docker container ls
```

# Upload your Docker Image to Docker Hub

## Tag your image

You might need to login before:
```bash
docker login
```

To associtate a local image with a repository on a registry (like Docker Hub) you should use the following tagging schema: username/repository:tag. The tag is optional, but recommended, since it is the mechanism that registries use to give Docker images a version.

Exchange the username rolandmmueller with your own Docker Hub user name and run:
```bash
docker tag bipm_hello rolandmmueller/bipm_hello:vers1
```

Check the newly tagged image
```bash
docker image ls
```
## Publish an image on Docker Hub

Exchange the username rolandmmueller with your own Docker Hub user name and run:
```bash
docker push rolandmmueller/bipm_hello:vers1
```

Check at https://hub.docker.com/ if your image is on Docker Hub.

You can run an image directly from a remote repository. If it is not locally present it will download (pull) it automatically.

Exchange the username rolandmmueller with the  Docker Hub user of one of your neighboring students (or your own if nobody is done yet):
```bash
docker run -p 4000:80 rolandmmueller/bipm_hello:vers1
```

Open in your browser http://localhost:4000/

## Create a stack of services with a docker-compose.yml file

Real world applications are build with multiple services that are interacting. For example, a Wordpress blog might at least use two services: the PHP Wordpress Blog and a MySQL database. Typically this two services would be two Docker images. Docker allows you to define this multi-service applications with a `docker-compose.yml` file. (see https://docs.docker.com/compose/overview/ for more infos about Docker compose)

We will enhance our little web application with a visitor counter. The count of visitors will be stored in Redis (https://redis.io/). Redis is a NoSQL database. Redis is an in-memory key-value database, used often as a cache or as part of a message broker.

Create in your `docker` folder a
`docker-compose.yml` file:

```yaml
version: '3'
services:
  web:
    build: .
    ports:
      - "4000:80"
    depends_on:
      - redis
    restart: always
    volumes:
      - ./app:/app
  redis:
    image: "redis:alpine"
    restart: always
```

`docker-compose.yml` is a YAML file and has the following elements:
*  The version of the `docker-compose.yml` file format (here it is version 3)
* Two services (the web application and the Redis database)
* The web service is build based on the Dockerfile in the current directory (`build: .`). Alternatively we could also use an image from Docker Hub (e.g. our own user image that we just pushed to Docker Hub)
* Port publishing of the container  port 80 to the host port 4000
* The second service is an offical Redis image from Docker Hu
* The web service starts after the Redis service, because it `depends_on` Redis.
* `restart: always`: Restarts the Web Server if it crashes or if the content of the app is changing. Restarts also the Redis Database after a crash.
* `volumes`: Maps the app folder in the host (your computer) to the app folder in the container. You can now just edit the content and the webpage should update without a new build of the container (just by reloading the page in the browser).

Change the `requirements.txt` file in the `app` folder:
```bash
Flask
Redis
```

Change the `app.py` file in the `app` folder:
```python
import time
import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello BIPM! I have been seen {} times.\n'.format(count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
```
* `cache = redis.Redis(host='redis', port=6379)`: Connext to the Redis datebase. As the host name we can use the service name from the `docker-compose.yml`file (`host='redis'`). The Redis connection is stored in the variable `cache`.
* The function `get_hit_count` will try to connect 5 time to connect to the Redis database.
* `return cache.incr('hits')` will increase the counter `'hits'` and then return the increased counter value. Redis is a Key-Value Database (similar to a dictionary in Python). `'hits'` is the key-name (could be any other name) and it will return the increased value for this key.
* `count = get_hit_count()`: stores the counter value in the variable `count`
* `return 'Hello BIPM! I have been seen {} times.\n'.format(count)`: Normal Python String interpolation. Variable `count` will be included in the `{}` position.

Run
```bash
docker-compose up
```

Open http://localhost:4000/

Refresh the page a couple of times.

# HTML Output with a Template

Add in the `app` folder  a `templates` folder. Create in the `templates` folder a file `hello.html` with the following content:
```html
<!doctype html>
<html>
	<link rel=stylesheet type=text/css href="{{ url_for('static', filename='style.css') }}">
   	<body>
    	<h1>I have been seen {{ count }} times.</h1>
    	<ul>
    		{% for i in range(1, count+1) %}
    			<li>{{ i }}: Hello {{ name }}! </li>
    		{% endfor %}
    	</ul>
    </body>
</html>
```
* The template uses a Python template engine named Jinja http://jinja.pocoo.org/
* This is just HTML with embedded Python
* You can embed variables with `{{ variable_name }}`. We will get from the render template function the variables `count` and `name`. `i` is just the loop variable.
* You can include Python control structures like loops or if-statements with `{% statement %}`
* if you have a loop (like a `for`) or if-statement, you need also an end statement (like `endfor`) because Jinja is not using indentation for ending blocks.
* `<link rel=stylesheet type=text/css href="{{ url_for('static', filename='style.css') }}">`: We create a link for the CSS style sheets. The CSS file is called `style.css` and is in the `static` folder. The function `url_for` creates the URL for this file.

Now let us add the CSS style. Add in the `app` folder  a `static` folder. Create in the `static` folder a file `style.css` with the following content:
```css
body { font-family: sans-serif; background: #eee; }
a, h1, h2 { color: #377ba8; }
h1, h2 { font-family: 'Georgia', serif; margin: 0; }
h1 { border-bottom: 2px solid #eee; }
h2 { font-size: 1.2em; }
ul { font-size: 0.8em;  }
```

Change the `app.py` file in the `app` folder:
```python
import time
import redis
from flask import Flask, render_template

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return render_template('hello.html', name= "BIPM", count = count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
```
* `return render_template('hello.html', name= "BIPM", count = count)`: instead of a string, we create a HTML page based on the template `hello.html`. We give the render_template function the variables `name` and `count`.

You can just refresh the browser without rebuilding the container, because your local app folder is mounted to the app folder in the container:

Open http://localhost:4000/

Refresh the page a couple of times.

If you change the image or if you are not using a mounted volume, you have to rebuild the images and rerun Docker compose: 
```bash
docker-compose build
```
and then  
```bash
docker-compose up
```

# Customize the Website

The final task is to customize the website like you want:
1. Add an image to the web page (hint: it works similar to the static CSS file)
2. Change some CSS
3. Maybe you have other ideas to change the website (see the Flask website for help http://flask.pocoo.org/docs/1.0/)
4. Create a screenshot of your web page and upload it to Moodle
