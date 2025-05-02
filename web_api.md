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
jupyterlab
requests
```
12.	Install the packages in your Python environment
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
•	200 – everything went okay, and the result has been returned (if any)
•	301 – the server is redirecting you to a different endpoint. This can happen when a company switches domain names, or an endpoint name is changed.
•	401 – the server thinks you’re not authenticated. This happens when you don’t send the right credentials to access an API.
•	400 – the server thinks you made a bad request. This can happen when you don’t send along the right data, among other things.
•	403 – the resource you’re trying to access is forbidden – you don’t have the right permissions to see it.
•	404 – the resource you tried to access wasn’t found on the server.

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

# Streamlit App

28.	Create a small Streamlit application that creates a dynamic website that shows the total number of people in space as well as all the names of the people. The app should use the API to get the names and display them. Add a descriptive title and a short description (you can use the Streamlit Markdown method).

29.	Add to your Streamlit app the following functionality:
a.	Get the current location of the International Space Station (ISS)
http://open-notify.org/Open-Notify-API/ISS-Location-Now/ 
b.	Create a geographical map in your Streamlit app that visualizes the current ISS location. There are a lot of different Python packages for geo-mapping. The easiest way in this scenario is to use the included map function in Streamlit: 
https://docs.streamlit.io/develop/api-reference/charts/st.map 
c.	Add a short description to your map

30.	Deploy your Streamlit app with CapRover to your VPS.  Create for your application a new subdomain `iss` so that your URL is something like `iss.example.com`. Enable HTTPS

31.	Copy-paste the URL of your deployed Streamlit app to Moodle

32.	What we have not covered in this exercise is authentication: A lot of Web APIs require a key for interacting with them (like OpenAI, Twitter, Facebook, …). You find at 
https://requests.readthedocs.io/en/latest/user/advanced
more information for Authentication for Web APIs with the request package. 
