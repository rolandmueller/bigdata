# Using a Web API with Python (Remote Procedure Invocation)

The four main service integration styles are
1.	File Transfer Integration,
2.	Integration through a Shared Database,
3.	Remote procedure invocation (Web API), and
4.	Message Queue.

This exercise shows how you can use a Web API with Python. Most Web APIs use a REST (REpresentational State Transfer) style, communicate over HTTP (Hypertext Transfer Protocol), and use JSON (JavaScript Object Notation) as a message format.

1.	https://randomuser.me/ is a random user generator
2.	It has an API. Go to https://api.randomuser.me/ with your browser
3.	You get a JSON back. A JSON is similar to a Python dictionary.  Refresh the browser
4.	You can add query parameters. They are added to the URL with a ? . You then add the parameter with parameter=value. If you have more than one parameter, then the parameters are connected with a & e.g.
	```http://www.example.com/api?lat=37.78&lon=-122.41```
5.	Go to the documentation https://randomuser.me/documentation and check how you can get multiple users and how to specify constraints on the output
6.	Go to your browser and add parameters to https://api.randomuser.me/ so that you get five results of only males from the US
8.	Now we want to analyze this data with Python
9.	Create in VS Code a new project
10.	Create a Python environment with uv and activate it
11.	Add a requirements.in file with the following packages:
```
pandas
matplotlib
python-dotenv
jupyterlab
streamlit
requests
```
12.	Install the packages in your Python environment
13. Create a `.gitignore` file (with `.` at the beginning) with the following content:
```sh
.env
venv
.venv
.idea
.ipynb_checkpoints
.vscode
.DS_Store
```
13.	Open a Jupyter Notebook and create a new notebook
14.	Import the library `requests` in your notebook
15.	You can find the documentation for the requests package here:
 https://docs.python-requests.org/en/latest/index.html
16.	With the requests package, you can call a Web API with the URL and the method get
```python
response = requests.get("https://api.randomuser.me/")
```
17.	Print the status code of the request
```python
print(response.status_code)
```
18.	The meanings of the status codes are:
* 200 – everything went okay, and the result has been returned (if any)
* 301 – the server is redirecting you to a different endpoint. This can happen when a company switches domain names, or an endpoint name is changed.
* 401 – the server thinks you’re not authenticated. This happens when you don’t send the right credentials to access an API.
* 400 – the server thinks you made a bad request. This can happen when you don’t send along the right data, among other things.
* 403 – the resource you’re trying to access is forbidden – you don’t have the right permissions to see it.
* 404 – the resource you tried to access wasn’t found on the server.

19.	Get with the request method 10 results of only males from the US. You can specify the query parameters with a Python dictionary like this:
```python
parameters = {"lat": 37.78, "lon": -122.41}
```
20.	And pass the parameter to the request like this
```python
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
```
This is the same as
```python
response = requests.get("http://api.open-notify.org/iss-pass.json?lat=37.78&lon=-122.41")
```
Alternatively, you could also build the URL also by yourself

21.	You can show the result of the request with the method text as a text (often good if the return is HTML, like for a website)
```python
response.text
```
22.	For a Web API, the return is most often JSON. You can convert the data from JSON to a Python dictionary with this:
```python
data = response.json()
```
23.	Check the type of variable data
24.	Loop through the dictionary and print all first names
25.	Print out all the names of the astronauts who are right now in space. You get the information about the Web APU from here
http://open-notify.org/Open-Notify-API/People-In-Space/
26.	Print the number of people that are right now in space
27.	Loop through the dictionary and print all first names
Use *pretty-print* (pprint). pprint prints complex data structures like a dictionary prettier.  https://docs.python.org/3/library/pprint.html
```python
from pprint import pprint
pprint(data)
```

# Financial Data with an API

Very often you need some kind of authentification for using an API (like for OpenAI, Twitter, Facebook, Payments, …). There are many different ways for authentification. One quite simple one is getting an API access token. This is kind of a password for accessing the service. You should not put any access tokens or passwords into your git source control. We will use again python-dotenv [python-dotenv](https://pypi.org/project/python-dotenv/) for managing the secretes and an `.env` file for storing the token

1. We will use Alpha Vantage https://www.alphavantage.co for getting some financial information.
2. Go to https://www.alphavantage.co/support/#api-key and get a free API key.
3. Create a new `.env` with the following content (change `DEMO` with your Alpha Vantage API Token that you got)
```bash
AV_TOKEN=DEMO
```

Add in your Jupyter Notebook a new cell for loading the Alpha Vantage API Token:

```python
import os
import requests
from dotenv import load_dotenv
import pandas as pd

load_dotenv()
av_token = os.getenv('AV_TOKEN')
```

Create a new cell in Jupyter Notebook for getting the Income Statement of a company as a JSON (Python dictonary)

```python
# Stock Ticker Symbol
symbol = 'AAPL'

url = f'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={symbol}&apikey={av_token}'
r = requests.get(url)
data = r.json()
data
```
Let us create out of the JSON a Pandas DataFrame

```python
income_df = pd.DataFrame(data['annualReports'])
income_df
```

Then we will do some preprocessin (extracting the year, changing the data type from string to float, and sorting it by year)
```python
income_df['fiscalDateEnding'] = pd.to_datetime(income_df['fiscalDateEnding'])
income_df['fiscalYear'] = income_df['fiscalDateEnding'].dt.year
cols_to_float = ['grossProfit', 'totalRevenue',
       'costOfRevenue', 'costofGoodsAndServicesSold', 'operatingIncome',
       'sellingGeneralAndAdministrative', 'researchAndDevelopment',
       'operatingExpenses', 'investmentIncomeNet', 'netInterestIncome',
       'interestIncome', 'interestExpense', 'nonInterestIncome',
       'otherNonOperatingIncome', 'depreciation',
       'depreciationAndAmortization', 'incomeBeforeTax', 'incomeTaxExpense',
       'interestAndDebtExpense', 'netIncomeFromContinuingOperations',
       'comprehensiveIncomeNetOfTax', 'ebit', 'ebitda', 'netIncome']

income_df[cols_to_float] = income_df[cols_to_float].apply(pd.to_numeric, errors='coerce')
income_df = income_df.sort_values(by='fiscalYear', ascending=True)
income_df
```

Then we can create a nice figure


```go
plt.style.use('fivethirtyeight')
fig, ax = plt.subplots(figsize=(10, 6))
income_df.plot(
    x='fiscalYear',
    y='totalRevenue',
    kind='bar',
    ax=ax,
    title=f'Revenue of {symbol}',
    ylabel='Revenue (Billion USD)',
    xlabel='Fiscal Year',
    legend=False
)

# Format y-axis to billions
ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x/1e9:.0f}'))

plt.tight_layout()
plt.show()
```

* Go up and change the symbol to 'META' and 'GOOG' and see how their revenue changed over the years.

* Look at https://www.alphavantage.co/documentation/ on how to get the daily adjusted full time series of the stock price. Plot it.

# Streamlit App

28.	Create a small Streamlit application that creates a dynamic website that shows the total number of people in space as well as all the names of the people. The app should use the API to get the names and display them. Add a descriptive title and a short description (you can use the Streamlit Markdown method).

29.	Add to your Streamlit app the following functionality:
a.	Get the current location of the International Space Station (ISS)
http://open-notify.org/Open-Notify-API/ISS-Location-Now/
b.	Create a geographical map in your Streamlit app that visualizes the current ISS location. There are a lot of different Python packages for geo-mapping. The easiest way in this scenario is to use the included map function in Streamlit:
https://docs.streamlit.io/develop/api-reference/charts/st.map
c.	Add a short description to your map

30.	Deploy your Streamlit app with CapRover to your VPS.  Create for your application a new subdomain `iss` so that your URL is something like `iss.example.com`. Enable HTTPS

31.	Copy-paste the URL of your deployed Streamlit app as well as the GitHub link to Moodle

