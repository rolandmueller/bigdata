# Creating a Web API with FastAPI

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
fastapi[all]
pydantic
uvicorn
httpx
pytest
pandas
scikit-learn
joblib
requests
jupyterlab
python-dotenv
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

* `def hello(name: str = ""):`: Now this function has a paramter `name` with a default value of an empty string `""`. Interesting is the so-called [**type hint**](https://docs.python.org/3.11/library/typing.html) `name: str`. Type hint is a standard way in Python to indicate (or hint) what data type a variable might have. Type hints in Python are optional (compared to languages like Java). `name: str` says that the input parameter should be a string. FastAPI is using type hints heavely for data validation and automatic type casting (transforming the input data type into the desired data type).

Open a browser or use Insomnia to test:
* GET http://127.0.0.1/hello?name=BIPM

The return value should be

```json
{"message": "Hello BIPM"}
```


## 3. Using POST and JSON Data

### 3.1 Modify main.py to use POST

In web development, GET and POST are two commonly used HTTP methods for client-server communication. A GET request is used to retrieve data from a server and typically includes parameters in the URL. The GET method is limited by URL length restrictions and cannot include a request body, which makes it unsuitable for sending large or complex data. Also a POST request is used to send data to the server. It can contain complex data like JSON or images.

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

### 3.2 Manually test with Insomnia

* POST to http://127.0.0.1/hello
* Body → JSON:

```json
{
  "name": "BIPM"
}
```

→ Response: {"message": "Hello BIPM"}

### 3.3 Add Documentation

You can add **docstrings** (https://peps.python.org/pep-0257/) to the functions, data types and web API endpoints. FastAPI uses this comments to auto-generate API docs.

Add comments:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Hello API",
    description="A simple FastAPI service that returns a greeting message based on the user's name.",
    version="0.1.0"
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

### 3.4 Add Automatic Tests with pytest

Tests are automated checks to verify that the code works as expected. Instead of manually checking if the system is still working as intended, we write code the check the actual result with the expected result. [Pytest](https://docs.pytest.org) is a powerful and easy-to-use testing framework for Python that supports simple unit tests as well as complex functional testing.

Create a folder `tests` with a file `test_hello.py`. A Python file for pytest MUST start with `test` or `test_`. Pytest will automatically detect these files and run all test in them.

`test_hello.py`

```python
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_hello_with_valid_name():
    response = client.post("/hello", json={"name": "John"})
    assert response.status_code == 200      # All OK
    assert response.json() == {"message": "Hello John"}
```

* `from fastapi.testclient import TestClient` - Imports FastAPI’s built-in test client for simulating HTTP requests in tests.
* `from app.main import app` - Imports the FastAPI application instance from your main.py file inside the app directory.
* `client = TestClient(app)` - Creates a test client that can interact with your FastAPI app as if it were a real HTTP client.
* `def test_hello_with_valid_name()` – Defines a test function that will be automatically discovered and run by pytest. Test functions MUST start with `test` or `test_`.
* `response = client.post("/hello", json={"name": "John"})` – Sends a POST request to the /hello endpoint with JSON data containing the name "John".
* `assert response.status_code == 200` – Asserts that the response has HTTP status code 200, meaning the request was successful. The `assert` statement in Python is used to check if a condition is true, and if it’s not, it raises an AssertionError, which helps detect bugs during testing or development.
* `assert response.json() == {"message": "Hello John"}` – Asserts that the returned JSON matches the expected greeting message.

run pytest in the Terminal with
```bash
pytest
```

Add three more tests in `test_hello.py`

```python
def test_hello_with_empty_name():
    response = client.post("/hello", json={"name": ""})
    assert response.status_code == 200
    assert response.json() == {"message": "Hello "}

def test_hello_missing_name_field():
    response = client.post("/hello", json={})
    assert response.status_code == 422

def test_hello_with_non_string_name():
    response = client.post("/hello", json={"name": 123})
    assert response.status_code == 422
```

* `assert response.status_code == 422` - checks that the HTTP response returned a 422 Unprocessable Entity status code, which means the server understood the request but couldn’t process it due to invalid or missing input data (typically from failed validation in FastAPI).

run pytest in the Terminal with
```bash
pytest
```

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

## 5. Add a Prediction Endpoint to your FastAPI App

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
  * Add a docsting as a comment and for the auto-generated documentation of the Web API. Also change the name, description, and version number of the overall app to reflect the new machine learning functionality.

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

### 5.2 Create a Unit Test for the new API

Create in `tests` a new file `test_api.py` and include unit tests for the machine learning API. Use the same input as in section 5.1 for the automatic tests.

Run all unit test in the Terminal with
```bash
pytest
```

## 5.3 Create an Authentification Token for the predict service

Create a `.env` file with the content (change DEMO to your secret)
```
API_TOKEN=DEMO
```

Add these lines in your code to load the value from the `.env` file

```python
from fastapi import FastAPI, Header, HTTPException
import os
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")
```

Change the predict function to:

```python
@app.post("/predict")
async def predict(features: IrisFeatures, x_api_token: str = Header(...)):
```
* `x_api_token`: This is a parameter name in the predict function that corresponds to a custom HTTP header called X-API-Token. It’s how the API expects clients to send the token.
* `Header(...)`: This is a dependency injection function from FastAPI that tells it to:
  * Extract the value of the X-API-Token HTTP header.
  * Inject it into the x_api_token variable.
  * The ellipsis `...` means this header is required.

Include in the predict function the following lines at the beginning:

```python
if x_api_token != API_TOKEN:
    raise HTTPException(status_code=401, detail="Unauthorized")
```

This code performs a basic security check to enforce API token authentication:
* x_api_token is the value sent by the client in the X-API-Token HTTP header
* API_TOKEN is the expected secret value loaded from your environment via `.env`.
* If they are not equal we will throw an exception and return status_code=401 ("Unauthorized").

Open Open http://127.0.0.1:80/docs and test the predict endpoint with the correct and not correct tokens.

## 5.4 Update the Tests

Check if the test still run
```bash
pytest
```

Of course they are not working anymore. So let us update the tests to reflect the new authentication logic.

Add in the test file at the top

```python
# Set up environment variable for testing
os.environ["API_TOKEN"] = "test-secret"
```

In the test, we just pretent that the API_TOKEN is "test-secret".

You have to update the `client.post` parameters and send the API token as a header (`headers={"X-API-Token": "test-secret"}`). Change your testing code similar to this:

```python
valid_payload = {
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
}

def test_predict_success():
    response = client.post(
        "/predict",
        json=valid_payload,
        headers={"X-API-Token": "test-secret"}
    )
    assert response.status_code == 200
    assert "prediction" in response.json()

def test_predict_invalid_token():
    response = client.post(
        "/predict",
        json=valid_payload,
        headers={"X-API-Token": "wrong-token"}
    )
    assert response.status_code == 401
    assert response.json()["detail"] == "Unauthorized"
```

* `headers={"X-API-Token": "test-secret"}`: Adds a custom header with the API token, required for authentication.

Check if the test are now running
```bash
pytest
```

## 6. Dockerize the FastAPI App

### 6.1 app/requirements.txt

```
fastapi[standard]
uvicorn
pydantic
pandas
scikit-learn
joblib
python-dotenv
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
* add in the App Configuration in CapRover https://caprover.com/docs/app-configuration.html#app-config as the environment variable  `API_TOKEN` and as the value your secrete token (e.g. `DEMO`). Save and update
* Visit https://iris.yourdomain.com/predict and test it in Insomnia

Check the documentation: https://iris.yourdomain.com/docs

## 7.3 README.md

Add a README.md file with a short description and a link to the deployed API and a link to the deployed API docs. Add the README.md file to Git and Commit and Push it to GitHub.

## Deliverables

Submit your GitHub URL to Moodle.
