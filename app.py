from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return 'Hello'

@app.route("/hola")
def ciao():
    return 'CIAO BELLA'


if __name__ == "__main__":
    app.run()
