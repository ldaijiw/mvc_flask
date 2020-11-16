# MVC with Flask in Python

## Model View Controller

MVC is a framework used for web development

![](images/mvc.jpg)

- The user is shown the front end, displayed any data in the browser using HTML, CSS, JS.
- The user makes a request to the _controller_ which in turn requests information from the database (_model_). - - The _model_ then sends the information back to the  _controller_
- The controller then sends the data to the _view_ which displays the response back to the user.

**MODEL**

- Using SQL Database

**VIEW**

- View in browser using HTML (Hyper Text Markup Language), CSS (Cascading Style Sheet), Javascript, and Bootstrap

**CONTROLLER**

- Using Python Flask


**Building our API**

- Display data from Python Flask to specific API call/URL/endpoint


## Flask

**Why Flask?**

- Flask is a web framework, a set of tools to build a web application
- It's very powerful to interact with the DB and user interface/browser
- Used to create an API
- Allows to integrate with HTML, CSS, JS
- Allows to map HTTP requests to Python functions
- Allows to set API path as a URL to view in the browser

### Setup

- Ensure it is installed with ``pip install flask``
- Run the flask app with ``flask run``
