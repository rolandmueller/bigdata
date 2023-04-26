# Creating a Web API with Python (Remote Procedure Invocation)

In this exercise we will not just consume an API, but create one with Flask. The steps are prity similar to the Docker/Flask exercise. The main difference is, that we do not return a HTML page but a JSON document. This tutorial is partially based on [this page](https://www.statworx.com/en/content-hub/blog/how-to-build-a-machine-learning-api-with-python-and-flask/).

An alternative to Flask is [FastAPI](https://fastapi.tiangolo.com/ ), which is an elegant and fast library to create Web APIs with Python. FastAPI uses Python [type hints](https://docs.python.org/3/library/typing.html) to infer the structure of the API from the function’s parameters. FastAPI creates also beautiful documentations of your API automatically. 

1. Create a folder `mlapi`, work inside the folder and open the folder in VS Code.

2. Open 

```python
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib
import numpy as np
```