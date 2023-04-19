
# Create a Streamlit App similar to Gapminder

You task is to create an interactive bubble chart with Streamlit, similar to Gapminder https://www.gapminder.org/tools/ 

## Requirements

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
1. population
2. Life expectancy
3. GNI per captia (PPP, current international $)

You have then 3 CSV files.

## Data Preprocessing

There are three things, you have to do, before building the dashboard. 
1. The data contains missing values. For all three CSVs, use forward filling for imputing the missing data. Forward filling uses earlier values of the country for filling later ones (tip: there exist a Pandas function for that)
2. For each CSV, transform the dataframe into a so called "tidy data format" (see e.g. https://en.wikipedia.org/wiki/Tidy_data). Each dataframe then should have only three columns: (1) country, (2) year, (3) the KPI (that means either a) life expectancy, b) population, or 3) GNI per capita)
4. You have to merge all three CVS.  Merge the three dataframe into one dataframe, that just has 5 columns (country, year and all three KPIs from the three dataframes)


## Streamlit App

Based on the requirements, create a Streamlit App

You can find more about Streamlit in this sources:
- https://calmcode.io/streamlit/hello-world.html
- https://docs.streamlit.io/en/stable/index.html
- https://streamlit.io/ 

### Charting in Streamlit

You can use different Python charting libraries in Streamlit, like Streamlit's own charting library, but also other Python packages like Matplotlib, Seaborn, Plotly or Bokeh. 

https://docs.streamlit.io/library/api-reference/charts

### Getting started
Create a new folder. 
Inside the folder, open a editor like PyCharm, Sublime or Visual Studio code https://code.visualstudio.com/
Have the whole folder as a project. 
Create a file `app.py` and enter a bare-bone Streamlit application:

```python
import streamlit as st
```

On the Terminal run

```bash
streamlit run app.py
```

When you change the code, you can just refrech the browser or enable autoupdate in Streamlit. 

The data loading (and preprocessing) should be cached.

## Dockerize your Streamlit App

Create a Dockerfile for your Streamlit App. Run and test the Docker container.

More information about how to Dockerize a Streamlit App:
* https://blog.jcharistech.com/2020/01/08/how-to-deploy-streamlit-apps-with-docker/
* https://www.youtube.com/watch?v=doCia_CKcko

Some tips:

Use a `requirements.txt` for managing your Python Packages:
e.g. `requirements.txt`:
```txt
streamlit
pandas
```

In the `Dockerfile` you can write somethin like this
```dockerfile
FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8501
ENTRYPOINT ["streamlit","run"]
CMD ["app.py"]
```

`pip install -r requirements.txt` is installing the Python packages inside the Docker container.

## Deliverable

1. Push your Strimlit directory to Github and post the URL of your repository to Moodle
2. Take a screenshot of the Streamlit App and upload it to Moodle
