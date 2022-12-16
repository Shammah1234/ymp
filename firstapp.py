from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "My name is shammah <h1>SHAMMAH</h1>"

if __name__ == "__main__":
    app.run()
