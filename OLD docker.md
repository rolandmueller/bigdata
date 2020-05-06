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

All running containers:
```bash
docker container ls
```

All containers:
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

Starts a Docker container and an interactive Bash (some images have as a command line not Bash but a normal Shell `sh`. Normally you can always get the command line of a container.)
```bash
docker run -it ubuntu bash
```

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

Now again the container is ended.

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

Login to a running container (change the CONTAINER ID)
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
With
* `--name` you can give a container a name (e.g. ubuntu1)
* `-d` detaches the command line from the container so it is running in the background.

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

Run (Adjust the command for your path):
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


# A small Web App

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
    app.run(host="0.0.0.0", port=80)
```

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

You might to login before:
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

Exchange the username rolandmmueller with the  Docker Hub user of your neighboring students (or your own if nobody is done yet):
```bash
docker run -p 4000:80 rolandmmueller/bipm_hello:vers1
```

Open in your browser http://localhost:4000/

## Create a stack of services with a docker-compose.yml file

Real world applications are build with multiple services that are interacting. For example, a Wordpress blog might a at least use two services: the PHP Wordpress Blog and a MySQL database. Typically this two services would be two Docker images. Docker allows you to define this multi-service applications with a docker-compose.yml file.

We will enhance our little web application with a visitor counter. The count of visitors will be stored in Redis (https://redis.io/). Redis is a NoSQL database. Redis is an in-memory key-value database, used often as a cache or as part of a message broker.

Create in your `docker` foler a
`docker-compose.yml`:

```yaml
version: '3'
services:
  web:
    build: .
    ports:
     - "4000:80"
  redis:
    image: "redis:alpine"
```

The `docker-compose.yml` is a YAML file and has the following elements:
*  The version of the `docker-compose.yml` file format (it is version 3)
* Two services (the web application and the Redis database)
* The web service is build based on the Dockerfile in the current directory (`build: .`). Alternatively we could also use an image from Docker Hub (e.g. our own user image)
* Port publishing of the container  port 80 to the host port 4000
* The second service is an offical Redis image from Docker Hub

Change the `requirements.txt` file in the `app` folder:
```bash
Flask
Redis
```

Create the `app.py` file in the `app` folder:
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
    app.run(host="0.0.0.0", port=80)
```

Run
```bash
docker-compose up
```

Open http://localhost:4000/

Refresh the page a couple of times.

# Creating a Wordpress Blog with a connected MySQL database

Based on: https://docs.docker.com/compose/wordpress/

Create a new folder `my_wordpress` and change into teh folder

Create a `docker-compose.yml` file with the following content:

```yaml
version: '3.3'

services:
   db:
     image: mysql:5.7
     volumes:
       - db_data:/var/lib/mysql
     restart: always
     environment:
       MYSQL_ROOT_PASSWORD: somewordpress
       MYSQL_DATABASE: wordpress
       MYSQL_USER: wordpress
       MYSQL_PASSWORD: wordpress

   wordpress:
     depends_on:
       - db
     image: wordpress:latest
     ports:
       - "8000:80"
     restart: always
     environment:
       WORDPRESS_DB_HOST: db:3306
       WORDPRESS_DB_USER: wordpress
       WORDPRESS_DB_PASSWORD: wordpress
       WORDPRESS_DB_NAME: wordpress
volumes:
    db_data: {}
```

Run
```bash
docker-compose up -d
```

* `-d` Detach: command line is detached from the container

open http://localhost:8000 in a web browser

Login and enter required data. Create a post.

```bash
docker-compose down
```
removes the containers and default network, but preserves your WordPress database.

```bash
docker-compose down --volumes
```
also removes the WordPress database.

# Using an existing Docker Container

```bash
docker run --name my-nginx -d -p 8080:80 nginx
```
* `-d` Detach: command line is detached from the container
* `-p` Publish Port: Publish your machine’s port 8080 to the container’s published port 80
* `--name` gives the container a name (here `my-nginx`)

Open in your browser `http://localhost:8080/`

The container is still running:
```bash
docker container ls
```

We can log in to the running container.
```bash
docker exec -it my-nginx bash
```
We can get out again with
```bash
exit
```

```bash
docker volume create website
```
