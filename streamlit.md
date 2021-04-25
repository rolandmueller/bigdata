
# Create a Streamlit App

You task is to create a interactive bubble chart with Streamlit similar to https://www.gapminder.org/tools/ 

## Requirements

The dashboard should have the following interactive widgets:
1. a year slider to control the year
2. a multiselect widget for selecting one or more countries

The dashboard does **NOT** to have to be animated (like the gapminder one).

The chart should have show the following KPIs:
1. On the x-axis: the logarithmic Gross Natition Income (GNI) per captia (inflation-adjusted and converted to $ based on purchasing power parity (PPP)). The maximal x value should be constant independent what you select, so that you can more easily compare the charts.
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

There are two things, you have to do, before building the dashboard. 
1. The data contain missing values. For all three CSV, use forward fill, to use earlier KPIs for the country for filling later ones (there is a Pandas function for that)
2. We have to merge all three CVS. For each CSV, transform the dataframe into a tidy format, with only three columns: (1) country, (2) year, (3) the KPI (that means either a) life expectancy, b) population, or 3) GNI per capita)
3. Merge the three dataframe into one dataframe, that just has 5 columns (country, year and all three KPIs)


## Streamlit App

Create based on the requirements the Streamlit App

You can find more about Streamlit in this sources:
- https://docs.streamlit.io/en/stable/index.html
- https://streamlit.io/ 
- https://calmcode.io/streamlit/hello-world.html

## Dockerize your Streamlit App

Create a Dockerfile for your Streamlit App and try it out.

Some tips:

Use a `requirements.txt`for managing your Python Packages:
requirements.txt:
```txt
streamlit
pandas
```

In the Dockerfile you can than use 
```dockerfile
RUN pip install -r requirements.txt
```
to install the Python packages inside the Docker container.

## Deliverable

Take a screenshot of the Streamlit App and upload it to Moodle
