# Docker

Docker has mainly three advantages:
* Reproducibility of the working environment. A colleague can easily reproduce the exact context of the code.
* Deployment of the work to the cloud 
* Create a solution that consists of multiple services. For example, a web server (like Flask) that stores data in a database (like PostgreSQL or Redis).

##  VS Code: Extension, creating a project and a folder

* Open VS Code

* In VS Code: Go to the extensions tab, search for Docker (from Microsoft) and install the Docker extension
* Create a new project with a new folder called `docker`
* Open in VS Code a Terminal (command line) (menu Terminal | New Terminal)

## Install and Login

* [Install Docker Desktop](https://docs.docker.com/desktop/)
* Create a Login at Docker Hub
* Start your Docker Program on your computer
* Login in Docker locally
* In the command line

```bash
docker login
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

log out of the container by entering
```bash
exit
```

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

Restart the container (change the name or use the CONTAINER ID in YOUR (!) list)
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

Login to an already running container with `docker exec` (change the CONTAINER ID in your (!) list);
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

### Containers and images

Let us start three different containers from the same image. 
Meaning of the parameters:
* `-it` interactive
* `--name` gives a container a name (e.g. ubuntu1)
* `-d` Detach: detaches the command line from the container so it is running in the background.


```bash
docker run -it -d --name ubuntu1 ubuntu bash
```
```bash
docker run -it -d --name ubuntu2 ubuntu bash
```
```bash
docker run -it -d --name ubuntu3 ubuntu bash
```


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
In the terminal of container ubuntu1 create a folder
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

## Define a new Image

Create a file with the name `Dockerfile` with the following content (e.g. with an IDE (integrated development environment) or editor like  Visual Studio Code or PyCharm). A Dockerfile tells Docker [how to build a Docker image](https://docs.docker.com/engine/reference/builder/).
You might be able to open an editor from the terminal directly (might be configure before in the IDE). 
* For opening VS Code in the current folder you can type in the terminal: `code .`
* For opening PyCharm type: `charm .` 
* The `.`mean the current folder


```bash
# Use an official Python runtime as a parent image
FROM python:3

# Set the working directory to /app
WORKDIR /app

# Copy the app directory contents into the container at /app
COPY app/ /app

# Run computation.py when the container launches
CMD ["python", "computation.py"]
```

Create the `app` folder and change into the folder
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

## Run Docker containers

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

## Volumes

To more easily attach data to an image but also store resulting data (e.g. from a computation or from a database) independent of the lifetime of the image, we can use volumes.

We can mount an volume when you run an image with the `-v` parameter. However, only absolute paths are possible. So first check out our current path with `pwd` (print working directory)
```bash
pwd
```
In my case, it is `/Users/rolandmueller/Documents/sourcecode/bigdata/docker`

Adjust the command for your path:
```bash
docker run -v /Users/rolandmueller/Documents/sourcecode/bigdata/docker/app/:/app bipm_compute
```

The `-v` flag expects two directories before and after the `:`. On the left of the `:` is the absolute path to a directory on the host system (your laptop) that will be mounted to an directory in the container (right side of `:`)

On Mac you might have to give file access to Docker. You can change this in the Privacy and Security Settings and restart Docker.

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

Run again (or use your absolute path) (you can go back in history in the terminal with the arrow keys):
```bash
docker run -v `pwd`/app/:/app bipm_compute
```
You should see the new result with building the container again.

## Named Volumes

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

* List all containers (you have to figure out the command)
* Delete the last created container (you have to figure out the command)

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

Exit
```bash
exit
```

# Create a small Flask Web App

We will build a web application with `Flask` (https://flask.palletsprojects.com/en/2.3.x/) (Partially based on https://docs.docker.com/compose/gettingstarted/). 

Create a `requirements.txt` file in the `app` folder. Here we can specify all python `pip` packages that we need. Add in the first line in the `requirements.txt` file:
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
* `from flask import Flask`: Imports the Flask class
*  `app = Flask(__name__)`: Creates the Flask object `app` that represent the main application
* @app.route('/'): This is a Python decorator. Python decorators (starting with `@`) are functions that change the behavior of other functions (https://realpython.com/primer-on-python-decorators/). Python decorators are  useful for example for logging or monitoring a function or calling a function via a web interface. Here we specify the web routing, that means what URL-path should call what function. Here we want, that the root URL (e.g. http://localhost/) should call the hello function. We could also link the function to any other URL-path like "/hello" so that the URL would be e.g. http://localhost/hello.
* `if __name__ == "__main__":` If we call a Python file with e.g. `python app.py`, the Python interpreter will assign the string `"__main__"` to the variable `__name__`. That means that this if statement will only be executed if it is run directly (and not if Python code is e.g. loaded as a module in another code).
* `app.run(host="0.0.0.0", port=80, debug=True)`: The Flask server starts and listens to port 80 and the debug mode is turned on.

# Running Flask with Docker

Change the `Dockerfile` file:

```dockerfile
# Use an official Python runtime as a parent image
FROM python:3

# Set the working directory to /app
WORKDIR /app

# Copy requirements.txt into the container at /app
COPY app/requirements.txt requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY app/ /app

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

With the container ID you can stop the running container (Use your CONTAINER ID):
```bash
docker container stop ccf9e14d3f3a
```

Check if the container is still running:
```bash
docker container ls
```

# Create a stack of services with a docker-compose.yml file

Real world applications are build with multiple services that are interacting. For example, a Wordpress blog might at least use two services: the PHP Wordpress Blog and a MySQL database. Typically this two services would be two Docker images. Docker allows you to define this multi-service applications with a `docker-compose.yml` file. (see https://docs.docker.com/compose/overview/ for more infos about Docker compose)

We will enhance our little web application with a visitor counter. The count of visitors will be stored in Redis (https://redis.io/). Redis is a NoSQL database. Redis is an in-memory key-value database, used often as a cache or as part of a message broker.

Create in your `docker` folder a
`docker-compose.yml` file:

```yaml
services:
  redis:
    image: redislabs/redismod
    ports:
      - '6379:6379'
  web:
    build: .
    stop_signal: SIGINT
    ports:
      - '4000:80'
    volumes:
      - ./app:/app
    depends_on:
      - redis
```

`docker-compose.yml` is a YAML file and has the following elements:
* Two services (the Redis database and the web application )
* The first service is an offical Redis image from Docker Hub
* Port publishing of the container port 6379 to the host port 6379
* The web service is build based on the Dockerfile in the current directory. Alternatively we could also use an image from Docker Hub (e.g. our own user image that we just pushed to Docker Hub)
* flask requires SIGINT to stop gracefully (default stop signal from Compose is SIGTERM)
* Port publishing of the container  port 80 to the host port 4000
* `volumes`: Maps the app folder in the host (your computer) to the app folder in the container. You can now just edit the content and the webpage should update without a new build of the container (just by reloading the page in the browser).
* The web service starts after the Redis service, because it `depends_on` Redis.
* `restart: always`: Restarts the Web Server if it crashes or if the content of the app is changing. Restarts also the Redis Database after a crash.

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
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>My first dynamic Website</title>
    <link rel="stylesheet" href="https://cdn.simplecss.org/simple.min.css">
</head>

<body>
    <main>
        <h1>I have been seen {{ count }} times.</h1>
        <ul>
            {% for i in range(1, count+1) %}
            <li>{{ i }}: Hello {{ name }}! </li>
            {% endfor %}
        </ul>
    </main>
</body>

</html>
```
* The template uses a Python template engine named Jinja http://jinja.pocoo.org/
* This is just HTML (HyperText Markup Language) with embedded Python. HTML is the language of the World Wide Web.
* HTML is just text with  opening tags (e.g `<head>`) and closing tags (e.g `</head>`). HTML tags are not shown directly in the Web browser, but only interpreted and used for formatting. A HTML page has two main parts: the head with meta data (e.g. with the styles, the title of the page) and the body with the main text and maybe also a navigation. 
* `<link rel="stylesheet" href="https://cdn.simplecss.org/simple.min.css">`: We create a link for an existing CSS style sheet and use https://simplecss.org/. Alternatively we could create or customize our own CSS style. CSS stands for Cascading Style Sheets and is the way how Web pages are designed. 
* `<meta charset="utf-8" />`: We will use UTF-8 for the characters.
* `<meta name="viewport" content="width=device-width, initial-scale=1" />`: Setting the viewport to make your website look good on mobile devices
* `<title>My first dynamic Website</title>`: This is the title of the web page. It will be displayed in the tab name in the browser and will appear in the search engine results
* You can embed variables with `{{ variable_name }}`. We will get from the render template function the variables `count` and `name`. `i` is just the loop variable.
* You can include Python control structures like loops or if-statements with `{% statement %}`
* if you have a loop (like a `for`) or if-statement, you need also an end statement (like `endfor`) because Jinja is not using indentation for ending blocks.


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

# Source controll with Git and Github

A `.gitignore` file is used in Git repositories to specify which files and directories should be excluded from version control. By listing patterns of files or directories that you don't want to track, you can prevent unwanted files like temporary files, build artifacts, logs, or sensitive configuration files from being included in your repository. This helps keep your repository clean and focused on the source code and relevant files.

Create a `.gitignore` file (with `.` at the beginning) with the following content:

```sh
.env
venv
.venv
.idea
.ipynb_checkpoints
.vscode
.DS_Store
```

A `.dockerignore` file is used to specify files and directories that should be excluded from the build context when creating a Docker image. This can help reduce the size of the build context, improve build performance, and prevent sensitive or unnecessary files from being included in the image. 

Create a `.dockerignore` file with the following content:
```sh
.env
venv
.venv
.idea
.ipynb_checkpoints
.vscode
.DS_Store
.git
.gitignore
```

In VS Code, click on the Source Controll side icon (on the left side). Click on the button `Initialize Repository`.

Now you should see at the Source Controll panel 9 files that are not yet checked in. Click on the `+` symbole next to Changes, to stage all files. Enter a Commit Message and commit the changes. Then publish the branch to Github. Check on Github that the repository is now there.

# Add a Password to the Database

Right now Redis is not secured through a password. This is right now not a problem, because everything is running on the laptop and we do not have any sensible data in the database. However, when we will deploy the app to a cloud provider, it is better to use a password for accessing the database.

Typically we do not want any plain-text password in the source code. The alternative is using environment variables (variables from the operation systems) or password files that we do not add into the source repository (often hidden files (that start with a `.` in the file name) with the name `.env`).

Create a new file in the docker folder (not in the app folder) with the name `.env` (with a `.` at the beginning), with the following content (you should use your own secrete password):

```bash
REDIS_PASSWORD=MyBIPMPassword
REDIS_HOST=redis
```

Adjust the `docker-compose.yml`file:
```yaml
services:
  redis:
    image: redislabs/redismod
    ports:
      - '6379:6379'
    command: --requirepass ${REDIS_PASSWORD}
  web:
    build: .
    stop_signal: SIGINT
    ports:
      - '4000:80'
    volumes:
      - ./app:/app
    depends_on:
      - redis
    environment:
      - REDIS_PASSWORD=${REDIS_PASSWORD}
      - REDIS_HOST=${REDIS_HOST}
```

`${REDIS_PASSWORD}` and `${REDIS_HOST}` will read the environment variables from the `.env` file.

Change the `requirements.txt` file by adding one more Python package [python-dotenv](https://pypi.org/project/python-dotenv/). 
```
Flask
Redis
python-dotenv
```

python-dotenv allows to either use environment variables or hidden files (`.env`) for things like passwords.

Change the `app.py` file.  Add the following lines:
```python
from dotenv import load_dotenv

load_dotenv() 
cache = redis.Redis(host=os.getenv('REDIS_HOST'), port=6379,  password=os.getenv('REDIS_PASSWORD'))
```

This loads the environments and with `os.getenv('REDIS_HOST')` and `os.getenv('REDIS_PASSWORD')` we can use the host name and the password in the Python code.

The `app.py` file should now look like this:

```python
import time
import redis
from flask import Flask, render_template
import os
from dotenv import load_dotenv

load_dotenv() 
cache = redis.Redis(host=os.getenv('REDIS_HOST'), port=6379,  password=os.getenv('REDIS_PASSWORD'))
app = Flask(__name__)

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

Try it out with 

```bash
docker-compose build   
```

and then

```bash
docker-compose up
```

and open the project in a web browser.

If it works, cancel the service in the terminal (control+C). In VS Code, add all changes to git and commit and push the changes.

# Customize the Website

The final task is to customize the website like you want (see https://simplecss.org/demo for help about Simplecss and https://flask.palletsprojects.com/en/2.3.x/ about Flask):
1. Add a link in `hello.html` that points to the HWR Berlin homepage
2. Add a footer with your name
3. Add an image to the web page. You can serve static files like images or CSS files with Flask: https://flask.palletsprojects.com/en/2.3.x/quickstart/#static-files
4. Add a navigation menu to the web page, with three menu items: Home (the current hello page), Titanic (another internal page) and About (a link to your Github homepage)
6. Create another page for the Titanic link (similar like the hello page). You have to add a new `titanic` function in `app.py`, but change the route to e.g. `/titanic`. This will tell what URL paths are mapped to this function.  Add a new `titanic.html` template. Add the CSV (comma seperated) file of the Titanic Dataset to your project. Use Pandas to load the CSV file and show the first 5 rows in the Titanic page. You can use the DataFrame method to_html https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_html.html 
7. Add a bar chart to the Titanic page, that shows how many men and women survived.
8. Create in the `docker` folder (not in the `app` folder) a `README.md` file. The ending `.md` stands for [markdown](https://www.markdownguide.org/basic-syntax/) and is a simple markup language. Add a short description of the project. Github will show the `README.md` file for the repository.
9. Push everything to Github.

# Deliverables

* Add the link to your Github repository to Moodle. 
* Create two screenshots of your web page (Home and Titanic) and upload them to Moodle too.
