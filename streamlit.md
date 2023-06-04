# Create a Streamlit App similar to Gapminder

You task is to create an interactive bubble chart with Streamlit, similar to Gapminder https://www.gapminder.org/tools/ and deploy it to the cloud.


# Docker Working Environment

Create a folder `gapminder`. Open this folder in VS Code (e.g. type in the folder in the terminal `code .`). Create in VS Code the following files with the content:

`.gitignore`: 
```bash
.env
venv
.idea
.ipynb_checkpoints
.vscode
.DS_Store
```

`.dockerignore`: 
```bash
.env
venv
.idea
.ipynb_checkpoints
.vscode
.DS_Store
.git
.gitignore
```

`Dockerfile`:
```dockerfile
# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy requirements.txt into the container at /app
COPY app/requirements.txt requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY app/ /app

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Run app.py when the container launches
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

`captain-definition`:
```json
{
    "schemaVersion": 2,
    "dockerfilePath": "./Dockerfile"
}
```

Create an `app` folder inside the `gapminder` folder.

In the `app` folder, create the following files with the content:

`requirements.txt`:
```txt
streamlit
pandas
```

`app.py`:
```python
import streamlit as st
import pandas as pd

st.title('Gapminder')
```

Now we will build the Docker image. Run in the terminal:
```bash
docker build -t gapminder .
```

On the comand line, we will run the Docker container and attach the `app` folder as a volume. With this trick, we can change the source code of the `app.py` file and just refresh the browser and see the change, without rebuilding the Docker image.

In the terminal, run

```bash
pwd
```

This will show the absolute path. (e.g. `/Users/rolandmueller/Documents/source/gapminder`) In the next step you have to use the abolute path of the `app` folder, that means in my case `/Users/rolandmueller/Documents/source/gapminder/app` and map it to the Docker folder `/app`. Change this folder in the next command based on your path:

```bash
docker run -p 8501:8501 -v /Users/rolandmueller/Documents/source/gapminder/app:/app gapminder
```

Open the URL http://0.0.0.0:8501

Let the terminal running and change the `app.py` file by adding at the end the following line:

```py
st.write("Unlocking Lifetimes: Visualizing Progress in Longevity and Poverty Eradication")
```

Refresh the browser to show the changes. You do not have to rebuild the Docker image, because the app folder is mounted as an external volume. 

You can find the meaning of the different Streamlit methods here: https://docs.streamlit.io/library/api-reference 

# Requirements

The dashboard should have the following interactive widgets:
1. a year slider to control the year (only one year will be displayed)
2. a multiselect widget for selecting one or more countries

The dashboard does **NOT** to have to be animated (like the Gapminder one).

The bubble chart should show the following KPIs:
1. On the x-axis: the **logarithmic** Gross Natition Income (GNI) per captia (inflation-adjusted and converted to $ based on purchasing power parity (PPP)). The maximal x value should be **constant** independent what you select, so that you can more easily compare the charts.
2. On the y-axis: Life expectancy
3. Size of the bubble: population
4. Color: Country

## Data Source

Download the data here: https://www.gapminder.org/data/

Go to "Choose individual indicators", choose the KPIs and download the CSV, for each KPI
1. Population
2. Life expectancy
3. GNI per captia (PPP, current international $) (Gross National Income per capita based on Purchasing Power Parity in current international dollars (inflation adjusted).)

You have then 3 CSV files.

## Data Preprocessing

There are three things, you have to do, before building the dashboard. 
1. The data contains missing values. For all three CSVs, use forward filling for imputing the missing data. Forward filling uses earlier values of the country for filling later ones (tip: there exist a Pandas function for that)
2. For each CSV, transform the dataframe into a so called "tidy data format" (see e.g. https://en.wikipedia.org/wiki/Tidy_data). Each dataframe then should have only three columns: (1) country, (2) year, (3) the KPI (that means either a) life expectancy, b) population, or 3) GNI per capita)
4. You have to merge all three CVS.  Merge the three dataframe into one dataframe, that just has 5 columns (country, year and all three KPIs from the three dataframes)

The data loading and preprocessing should be cached. https://docs.streamlit.io/library/api-reference/performance/st.cache_data 

### Streamlit Docs

Based on the requirements, create a Streamlit App

You can find more about Streamlit in this sources:
- https://docs.streamlit.io/
- https://docs.streamlit.io/library/api-reference
- https://calmcode.io/streamlit/hello-world.html

You can use different Python charting libraries in Streamlit, like Streamlit's own charting library, but also other Python packages like Matplotlib, Seaborn, Plotly or Bokeh. 

https://docs.streamlit.io/library/api-reference/charts

When you have finished the app according to the requirements, you should push it to Github and deploy it to a cloud server. 

# Adding code to Git and Github

In VS Code, click on the Source Controll side icon (on the left side). Click on the button `Initialize Repository`. Now you should see at the Source Controll panel files that are not yet checked in. Click on the `+` symbole next to Changes, to stage all files. Enter a Commit Message and commit the changes. Then publish the branch to Github.

# Deployment of your Streamlit app to CapRover

1. Create at the CapRover Web GUI a new app with the name `gapminder`
2. Enter for the app, at `Container HTTP Port`: 8501  (The Streamlit Docker container exposes Port 8501)
3. Enable with the checkmark `Websocket Support` (This is important because Streamlit is using Websockets)
4. Click `Save & Update`
5. On the local terminal in the gapminder folder, run 
```bash
caprover deploy
```
Chose `gapminder` as the app and deploy your solution.

6. Go back to the CapRover Web GUI and check the URL of the `gapminder` app. Does it work?

7. Create at your domain provider (e.g. Namecheap) a new subdomain (like `gapminder` (without a wild card (star) before)) and point it to the same IP-address of your VPS. In the CapRover Web GUI for the gapminder app, add the full domain (e.g. gapminder.example.com) and clock on `Connect New Domain`. Test if you can reach your app also to the new app (e.g. at http://gapminder.example.com).

8. In the CapRover Web GUI for the newly added domain (e.g. at http://gapminder.example.com), click `Enable HTTPS`. Test if you can reach your app with the https URL (e.g. at https://gapminder.example.com).

9. In the CapRover Web GUI, enable `Force HTTPS by redirecting all HTTP traffic to HTTPS`. Enter your domain without https (e.g. at http://counter.example.com) and test if you get redirected to the https URL (e.g. to https://counter.example.com).

10. Add a `README.md` file, with a short description and a link to the deployed prototype.

# Deliverables

* Add the URL to the Github Repository 
* and the URL to your deployed prototype in the Moodle
