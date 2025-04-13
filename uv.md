# How to start with **uv**

For a complete documentation look at the [uv webpage](https://docs.astral.sh/uv/).

1. In the project folder, create a virtual enviroment

```
uv venv
```

2. Activate the enviroment

On Mac:
```
source .venv/bin/activate
```

On Windows:
Depends on your shell (follow uv instruction).

For PowerShell on Windows:
```
.venv\Scripts\Activate.ps1
```

3. Create a **requirements.in** file

In this fill you can include all the Python package names that you need. You can also specify the version number if you like, e.g.:

```
pandas
scikit-learn
jupyterlab
matplotlib
seaborn
```

4. Compile the requirements.in and save it to requirements.txt

```
uv pip compile requirements.in > requirements.txt
```

5. Install the packages in the environment with **sync**

```
uv pip sync requirements.txt
```





