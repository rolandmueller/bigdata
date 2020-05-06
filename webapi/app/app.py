from flask import Flask
from flask import request, jsonify

app = Flask(__name__)

courses = [
    {'id': 0,
     'title': 'Data Science',
     'professor': 'Markus Löcher',
     'semester': '1'},
    {'id': 1,
     'title': 'Data Warehousing',
     'professor': 'Roland M. Mueller',
     'semester': '1'},
    {'id': 2,
     'title': 'Business Process Management',
     'professor': 'Frank Habermann',
     'semester': '1'},
    {'id': 3,
     'title': 'Stratigic Issues of IT',
     'professor': 'Sven Pohland',
     'semester': '1'},
    {'id': 4,
     'title': 'Text, Web and Social Media Analytics Lab',
     'professor': 'Markus Löcher',
     'semester': '2'},
    {'id': 5,
     'title': 'Enterprise Architectures for Big Data',
     'professor': 'Roland M. Mueller',
     'semester': '2'},
    {'id': 6,
     'title': 'Business Process Integration Lab',
     'professor': 'Frank Habermann',
     'semester': '2'},
    {'id': 7,
     'title': 'IT-Security and Privacy',
     'professor': 'Dennis Uckel',
     'semester': '2'},
    {'id': 8,
     'title': 'Research Methods',
     'professor': 'Marcus Birkenkrahe',
     'semester': '2'},

]

@app.route('/api/v1/courses/all', methods=['GET'])
def api_all():
    return jsonify(courses)

@app.route('/api/v1/courses', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for course in courses:
        if course['id'] == id:
            results.append(course)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)