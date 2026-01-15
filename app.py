from flask import Flask
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello DevOps, this has been a long journey!, let's try a newer version: v18."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

