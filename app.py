from flask import Flask, jsonify

# create an instance of our app, with __name__ passed as arg

app = Flask(__name__)

students = [
    {"id": 0, "title": "Mr.", "first_name": "Leo", "last_name": "Waltmann", "course": "DevOps"}
]

# use decorator to create API/url for user to access our data in the browser
# single forward slash indicates home (localhost:5000 is default port for Flask)
@app.route("/")
def home():
    return "<h1>Hello World</h1>"

# this function will run when the URL/API is accessed

# Creating our own API to display data on the specific route/URL/Endpoint/API
# will add URL to http://127.0.0.1:5000/api/v1/student/data
@app.route("/api/v1/student/data", methods = ["GET"])
def customised_api():
    # Extact Transform Load
    # Transforms data into JSON
    return jsonify(students)


if __name__ == "__main__":
    app.run(debug=True)