# Creating a Web API with FastAPI (Remote Procedure Invocation)

In this tutorial, you will create your own machine learning-powered Web API using [FastAPI](https://fastapi.tiangolo.com), a modern and high-performance framework for building APIs with Python. FastAPI replaces Flask from the previous GitHub and Docker examples, taking advantage of FastAPI’s data validation, automatic docs, and async support. FastAPI is the most common Python solution for exposing the backend. Alternatives are Flask and Django.

## 1. Project Setup

### 1.1 Create the project folder

Create and open a folder called `mlapi` in VS Code.

### 1.2 Create a virtual environment with uv

```bash
uv venv
```

Activate Mac:

```bash
source .venv/bin/activate
````

Activate Windows:

```bash
.venv\Scripts\Activate.ps1
````

### 1.3 Add dependencies

Create a `requirements.in` file:

```txt
fastapi
uvicorn
pandas
scikit-learn
joblib
requests
jupyterlab
```

Then compile and install it with:
```bash
uv pip compile requirements.in > requirements.txt
uv pip sync requirements.txt
```

## 2. Create the FastAPI App

### 2.1 Project Structure

Create the following structure:

```
mlapi/
├── app/
│   └── main.py
├── .gitignore
├── .dockerignore
```

### 2.2 Add .gitignore and .dockerignore

.gitignore and .dockerignore:

`.gitignore`

```
.env
.venv
.idea
.ipynb_checkpoints
.vscode
.DS_Store
.ipython
.local
.cache
.jupyter
.git
```

`.dockerignore`
```
.env
venv
.venv
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

### 2.3 Initial FastAPI App

`app/main.py`

```python
from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "Hello World"}
```

What is the meaning of the code:

* `app = FastAPI()`: This creates a new FastAPI application instance named `app`.
* 	`@app.get("/hello")`: This registers a GET endpoint at the path `/hello`. So it will listen to the URL path `localhost/hello` or `yourdomain.com/hello` The `@` symbol represents in Python a decorator, that modifies the behavior of another function without changing its actual code.
* `def hello():`: This defines a Python function named `hello` to handle requests to the /hello endpoint.
* `return {"message": "Hello World"}`: This returns a JSON response containing a greeting message.

On the fist look, FastAPI look quite similar to Flask (we used it in the Docker exercise). However, especially for data validation and automatic documentation of the API, FastAPI has couple of advantages compared to Flask.

### 2.4 Run the App


Start the FastAPI app using [Uvicorn](https:///www.uvicorn.org):

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 80
```

Open a browser or use Insomnia to test:
* GET http://127.0.0.1/hello

The return value should be

```json
{"message": "Hello World"}
```

### 2.5 Modify main.py by adding an input parameter to the route

Now we add a parameter to the URL route, so that we can send data to the server. In this case the name that we want to use to greet.

`app/main.py`
```python
from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

@app.get("/hello")
def hello(name: str = ""):
    return {"message": f"Hello {name}"}
```

* `def hello(name: str = ""):`: Now this function has a paramter `name` with a default value of an empty string `""`. Interesting is the so-called [**type hint**](https://docs.python.org/3.11/library/typing.html) `name: str`. Type hint is a standard why in Python to indicate (or hint) what data type a variable might have.  Type hints in Python are optional (compared to language like Java). `name: str` says that the input parameter should be a string. FastAPI is using type hints heavely for data validation and automatic type casting (transforming the input data type into the desired data type).

Open a browser or use Insomnia to test:
* GET http://127.0.0.1/hello?name=BIPM

The return value should be

```json
{"message": "Hello BIPM"}
```


## 3. Using POST and JSON Data

### 3.1 Modify main.py to use POST

In web development, GET and POST are two commonly used HTTP methods for client-server communication. A GET request is used to retrieve data from a server and typically includes parameters in the URL. The GET method is limited by URL length restrictions and cannot include a request body, which makes it unsuitable for sending large or complex data. Additionally, because data is exposed in the URL, GET is not secure for transmitting sensitive information. A POST request is used to send data to the server (usually in the request body), often for creating or processing resources.

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class NameRequest(BaseModel):
    name: str

@app.post("/hello")
def hello(data: NameRequest):
    return {"message": f"Hello {data.name}"}
```

* `from pydantic import BaseModel`: The `pydantic` library is used for data validation in FastAPI. `BaseModel` is a class from [Pydantic](https://docs.pydantic.dev/latest/) that provides automatic data validation, parsing, and error handling based on Python type hints.
*
```python
class NameRequest(BaseModel):
    name: str
```

  This defines a Pydantic model NameRequest that expects a JSON object with a name field of type string.

* `@app.post("/hello")`: registers a POST endpoint at the path `/hello` in the FastAPI application
* `def hello(data: NameRequest):`: defines a function `hello` that takes a `NameRequest` object (parsed from incoming JSON) as input.
* `return {"message": f"Hello {data.name}"}`: returns a JSON response containing a personalized greeting using the name from the input data

### 3.2 Test with Insomnia

* POST to http://127.0.0.1/hello
* Body → JSON:

```json
{
  "name": "BIPM"
}
```

→ Response: {"message": "Hello BIPM"}

### 3.3 Adding Documentation

You can add **docstrings** (https://peps.python.org/pep-0257/) to the functions, data types and web API endpoints. FastAPI uses this comments to auto-generate API docs.

Add comments:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Hello API",
    description="A simple FastAPI service that returns a greeting message based on the user's name.",
    version="1.0.0"
)

class NameRequest(BaseModel):
    """
    Schema for input data containing a user's name.
    """
    name: str

@app.post("/hello", summary="Greet the user", response_description="A greeting message")
def hello(data: NameRequest):
    """
    Returns a personalized greeting message.

    Args:
        data (NameRequest): A JSON body with a `name` field.

    Returns:
        dict: A JSON response with a greeting message.
    """
    return {"message": f"Hello {data.name}"}
```

Open the automatically generates interactive documentation (Swagger UI). Open http://127.0.0.1:80/docs

You can even try out the API through the documents. Try it out.

## 4. Train and Save the ML Model

### 4.1 Create folder and download data

Createa a folder `dev`

Download the file `iris.csv`from Moodle and svae it in the `dev` folder

### 4.2 Create dev/01-training.ipynb and Load Data

In VS Code create a new Jupyter Notebook with the name `01-training.ipynb`:
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn import metrics
import joblib

data = pd.read_csv('iris.csv')

y = data['species']
X = data.drop(columns=['species'])

# TODO
# Train test split with 30% text and a random state of 23

# Create an median Imputer

# Create an instance of a ColumnTransformer that applys the Imputer on all columns

# Create a Random Forest Classifier (with random state 23)

# Create a pipeline with the ColumnTransformer as a preprocessor and the Random Forest Classifier as a classifier

# Train the pipeline on the training data

# Predict the results on the test data

# print a classification report

# save the the pipeline in the app folder
joblib.dump(pipe, '../app/iris.mdl')
```

Check how good the accuracy, precision, recall, and F1 score is?

## 5. Add a Prediction Endpoint to Your FastAPI App

In this exercise, you will extend your FastAPI application by creating a new endpoint that accepts input data for an iris flower and returns a machine learning prediction of the species.

**Goal:**

Update `app/main.py` by creating a new POST endpoint `/predict` that:
* Accepts input data in JSON format (with four numerical features)
* Converts the data into a Pandas DataFrame
* Uses a pre-trained model (iris.mdl) to make a prediction
* Returns the predicted species as a JSON response

**Steps:**

* Make sure your trained model file (iris.mdl) is saved in the app folder from the previous training step.
* Load the saved ML model into your app. You can do this outside of the `predict` function, so that this is only done once.
* Define a Pydantic model to validate the four input fields (all floats).
* Extend your FastAPI app with a new endpoint `predict`:
  * Convert the incoming request data (JSON) into a Pandas DataFrame. You can get the data as an dict with `data.dict()`
  * Use the loaded model to make a prediction.
  * Return the prediction as a JSON response.
  * Add a docsting as a comment and for the auto-generated documentation of the Web API.


### 5.1 Test in Insomnia

POST http://127.0.0.1/predict

```json
{
    "petal_length": 2,
    "sepal_length": 2,
    "petal_width": 0.5,
    "sepal_width": 3
}
```

→ Response: {"prediction": "Iris-setosa"}

Try with other data or missing data as well.

```json
{
    "petal_length": 1,
    "sepal_length": 4,
    "petal_width": 2,
    "sepal_width": 3
}
```

```json
{
    "petal_length": 1,
    "sepal_length": 4,
    "sepal_width": 3
}
```

```json
{
    "petal_length": 1,
    "sepal_length": "4",
    "petal_width": "2",
    "sepal_width": 3
}
```

Send also text instead of float into the endpoint. Check the results or errors.

```json
{
    "petal_length": "Hallo",
    "sepal_length": "BIPM",
    "petal_width": 2,
    "sepal_width": 3
}
```

Check the documentation: Open http://127.0.0.1:80/docs

## 6. Dockerize the FastAPI App

### 6.1 app/requirements.txt

```
fastapi
uvicorn
pandas
scikit-learn
joblib
```

### 6.2 Dockerfile

```docker
FROM python:3.10-slim-buster
WORKDIR /app
COPY app/requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY app/ /app
EXPOSE 80
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
```

### 6.3 docker-compose.yml

```yaml
services:
  web:
    build: .
    stop_signal: SIGINT
    ports:
      - "80:80"
    volumes:
      - ./app:/app
```

Run with:

```bash
docker-compose up
```

Test the API again in Insomnia.

## 7. Deploy with CapRover

### 7.1 Push to Git

Use VS Code Source Control:
* Initialize Git repo
* Commit your code
* Publish to GitHub

### 7.2 Deploy

In CapRover Web GUI:
* Create new app iris

In terminal:
```bash
caprover deploy
```

Select the app name and follow instructions.

Once deployed:
* Visit https://iris.yourdomain.com/predict and test it in Insomnia

## Deliverables

Submit your deployed FastAPI API URL on Moodle.
