from flask import Flask  
# Import the Flask class from the flask package to create a web application

app = Flask(__name__)  
# Initialize a Flask application instance. 
# __name__ tells Flask where to look for resources (templates, static files, etc.)

@app.route("/hello")  
# Define a route (URL endpoint) for "/hello". 
# When a client visits http://<host>:5000/hello, this function will be executed.

def hello():  
    return "Hello COPS team! This is a newer version. v49"  
    # Function that returns a plain text response to the client

if __name__ == "__main__":  
    app.run(host="0.0.0.0", port=5000)  
    # Run the Flask development server if this file is executed directly.
    # host="0.0.0.0" makes the app accessible externally (not just localhost).
    # port=5000 specifies the port where the app will listen.










