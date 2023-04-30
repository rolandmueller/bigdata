# Creating a Web API with Python (Remote Procedure Invocation)

In this exercise we will not just consume an API, but create one with Flask. The steps are prity similar to the Docker/Flask exercise. The main difference is, that we do not return a HTML page but a JSON document. This tutorial is partially based on [this page](https://www.statworx.com/en/content-hub/blog/how-to-build-a-machine-learning-api-with-python-and-flask/).

An alternative to Flask is [FastAPI](https://fastapi.tiangolo.com/ ), which is an elegant and fast library to create Web APIs with Python. FastAPI uses Python [type hints](https://docs.python.org/3/library/typing.html) to infer the structure of the API from the function’s parameters. FastAPI creates also beautiful documentations of your API automatically. 

1. Create a folder `mlapi`, work inside the folder and open the folder in VS Code.

2. We create a simple Flask API first. This is very similar to the Docker exercise. The difference is, that this Flask application will return JSON, not HTML.

We create the following files (exactly the same we as in the Flask example):
`Dockerfile`:
```dockerfile
# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Set the working directory to /app
WORKDIR /app

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

Create a `.gitignore` file (with `.` at the beginning) with the following content:

```sh
.env
venv
.idea
.ipynb_checkpoints
.vscode
.DS_Store
.ipython
.local
.cache
.jupyter
```

Create a `.dockerignore` file with the following content:
```sh
.env
venv
.idea
.ipynb_checkpoints
.vscode
.DS_Store
.git
.gitignore
.ipython
.local
.cache
.jupyter
```

`docker-compose.yml` file:
```yaml
services:
  web:
    build: .
    stop_signal: SIGINT
    ports:
      - '80:80'
    volumes:
      - ./app:/app
```

Create a `app` folder in the `mlapi`. Create the following files:

`requirements.txt` file:
```bash
Flask
```

Create the `app.py` file in the `app` folder:
```python
from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return {'message': 'Hello World'}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
```

The only difference to the Flask app from the former exercise, is that we return JSON. The line:
```python
    return {'message': 'Hello World'}, 200
```

Returns first a Python dictonary `{'message': 'Hello World'}`, that Flask is returning as JSON. The second value (`200`) is the HTTP return value, that means, everything went okay, and the result has been returned.

Run
```bash
docker-compose up
```

Download and install Insomnia https://insomnia.rest/download 

Open Insomnia. Enter http://127.0.0.1/hello in the URL field in Insomnia. Select GET. Click send.

You see on the right side, an `200 OK` result with the JSON return data.

Select POST (Dropdown left from the URL) and click send. You get the 405 error "Method Not Allowed"

Select GET and enter http://127.0.0.1/app and click send. You get the 404 error "Not Found".

Now we want to send a GET parameter. Change the code of `app.py`:

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/hello')
def hello():
    name = request.args.get('name', '')
    message = f'Hello {name}'
    return {'message': message}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
```

We import additionally the `request` module from the Flask package in the first line. Then we use the  `args` function to get the parameter arguments with:
```python
name = request.args.get('name')
```

Go to the Insomnia app and enter `http://127.0.0.1/hello` in the URL field. Click on the `Query` tab and enter the name value pair, `name` and `BIMP`. Click Send.

You should now see on the right: 
```json
{
	"message": "Hello BIPM"
}
```

Parameters in the URL are limited in size. Therefore it makes sense to use POST and JSON to also send data to the API.

Update `app.py`_ 
```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/hello', methods=['POST'])
def hello():
    data = request.get_json()
    name = data.get('name', '')
    message = f'Hello {name}'
    return {'message': message}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
```

We changed two things:
```python
@app.route('/hello', methods=['POST'])
```
This line says, that the function now accept the POST method.

```python
    data = request.get_json()
    name = data.get('name')
```
Now we want to send the data as JSON. The first line uses again the request modul but this time get the sended JSON data with `get_json`. This is then saved as a Python dictonary `data`. `data.get('name', '')` just gets the item with the `name` key from the dictonary and returns the value.

In Insomnia, add `http://127.0.0.1/hello` and change to POST (from GET). Delete any Query parameters, if any were still there. Click on the drop-down menu next to `Body` and select `JSON`. Copy this JSON into it field:

```json
{
	"name": "BIPM"
}
```

Check the results on the right side.

# Creating an API for a ML model

Great. Now we will train a machine learning model and expose the train mode with an API.

Create a new file in the `mlapi` folder with the name `docker-compose_jupyter.yml`:

```yaml
services:
  jupyter:
    image: jupyter/base-notebook:latest
    container_name: jupyter
    ports:
      - 8888:8888
    volumes:
      - ./:/home/jovyan
    environment:
      JUPYTER_ENABLE_LAB: "yes"
      JUPYTER_TOKEN: "docker"
```

We will use the [Iris flower data set](https://en.wikipedia.org/wiki/Iris_flower_data_set). The data set consists of 150 samples from three species of Iris water lily flowers (Iris setosa, Iris virginica and Iris versicolor). The dataset has four features: the length and the width of the sepals and petals. Download the `iris.csv` file from Moodle. Create in the `mlapi` folder a new `dev` folder and save `iris.csv` in this folder.

Change the content of `requirements.txt` (in the `app` folder):
```bash
Flask
pandas
scikit-learn
joblib
```

On the terminal, start the new docker compose file with
```bash
docker-compose -f docker-compose_jupyter.yml up
```

Open in the browser http://127.0.0.1:8888/  and if asked enter as the token "docker".

On the left side in Jupyter Lab, open the `dev` folder and create a new notebook in this folder. Rename it to `01-training.ipynb`.

The first cell should install the requirements:
```bash
%pip install -r ~/app/requirements.txt
```

Then in the next cell we import the requireed functions:
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn import metrics
import joblib
```

Read the iris.csv file as a DataFrame with the name `data`:
```python
data = pd.read_csv('iris.csv')
```

Save the label as y and the features as X:
```python
y = data['species']
X = data.drop(columns=['species'])
```

Train-test split:
```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=23)
```

Save Column Names:
```python
column_names = list(X_train.columns)
```

We create a simple imputer that uses the median value of the column for missing values:
```python
imp = SimpleImputer(strategy='median')
```

We apply this imputer on all columns:
```python
ct = ColumnTransformer([('imputer', imp, column_names)])
```
We will use a Random Forest as the classifier:
```python
clf = RandomForestClassifier(random_state=23)
```

The whole pipeline compines the preprocessing through the imputer and then the classifier:

```python
pipe = Pipeline([
    ('preprocessor', ct),
    ('classifier', clf)]
)
```

Now we can train the pipeline:
```python
pipe.fit(X_train, y_train)
```

To check the performance we will apply the trained pipeline to the test data and compare the prediction with the real results in the test data:
```python
y_pred = pipe.predict(X_test)
print(metrics.classification_report(y_test, y_pred))
```

How is the performance?

Save the model in the `app` folder:
```python
joblib.dump(pipe, '../app/iris.mdl')
```

Stop the Docker compose and close the Jupyter Lab Browser

Open VS Code and change the code of `app.py`:

```python
from flask import Flask, request
import joblib
import pandas as pd

app = Flask(__name__)
pipe = joblib.load('iris.mdl')

@app.route('/hello', methods=['POST'])
def hello():
    data = request.get_json()
    name = data.get('name')
    message = f'Hello {name}'
    return {'message': message}, 200

@app.route('/predict', methods=['POST'])
def predict():
    column_names = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
    data = request.get_json()
    data_vector = [data.get('sepal_length'), 
                   data.get('sepal_width'), 
                   data.get('petal_length'), 
                   data.get('petal_width')]
    X_new = pd.DataFrame([data_vector], columns=column_names)
    y_pred = pipe.predict(X_new)[0]
    return {'prediction': y_pred}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
```

We made the following changes:
- We imported `joblib` and `pandas`
- With `pipe = joblib.load('iris.mdl')` we load the pipeline from the stored `iris.mdl` file.
- We added the `predict()` function
- We define the column names
- Then we get the data as JSON
- Then we create a Python list based on the different features from the JSON data.
- Then we transform the Python list into a Pandas DataFrame
- With `pipe.predict(X_new)` we predict the species. Because we only have one row, we get the first row from the predictions: `pipe.predict(X_new)[0]`
- Then we return the prediction as JSON with a HTTP code 200.

In the command line, start you web server with:

```bash
docker-compose up 
```

Open Insomnia.

- On the left side, click on the arrow next to `New Request` and rename it to `Hello World`

- On the left side, under Cookies, click on the plus and then on `HTTP request`. Rename it to `Predict API`

- Change the HTTP method from GET to POST

- Enter http://127.0.0.1/predict in the URL

- Click on `Body` and select `JSON`

- Copy in the Body:

```json
{
    "petal_length": 2,
    "sepal_length": 2,
    "petal_width": 0.5,
    "sepal_width": 3
}
```

The result on the right side should be:
```json
{
	"prediction": "Iris-setosa"
}
```

Try out these values:
```json
{
    "petal_length": 5.8,
    "sepal_length": 2.6,
    "petal_width": 5.1,
    "sepal_width": 2.2
}
```

What about when you have missing data:
```json
{
    "petal_length": 5.7,
    "sepal_length": 2.8,
    "sepal_width": 1.3
}
```

Now let us deploy it.

In VS Code, click on the left on the Source Control icon. Click Initialize Repository. Click on the plus icon next to changes. Enter a commit message "Initial commit" and commit. Publish Branch.

Go to the CapRover Web GUI and create a app with the name `iris`. 

In you terminal, type 
```bash
caprover deploy
```

Chose the `iris` app and follow the instruction. 

Go to the CapRover Web GUI and copy the app URL.

Go to Insomnia and exchange `http://127.0.0.1/predict` your domain, e.g. 

with e.g. `http://iris.dev.example.com/predict` and try if it still works.

You might wait some seconds after the deploy until your server is ready. Just retry.