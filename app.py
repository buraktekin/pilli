from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/name")
def name():
    return "Burak"

if __name__ == "__main__":
    app.run()
