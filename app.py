from flask import Flask

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


if __name__ == "__main__":
    app.run(debug=True)