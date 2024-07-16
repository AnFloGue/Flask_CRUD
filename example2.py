from flask import Flask
from datetime import datetime

app = Flask(__name__)


HELLO_HTML = """
    <html><body>
        <h1>Hello, world!</h1>
        Click <a href="/time">HERE</a> for the time.
    </body></html>
    """


TIME_HTML = """
    <html><body>
        The time is {0}.
    </body></html>
    """


@app.route('/')
def hello():
    return HELLO_HTML


@app.route('/time')
def time():
    return TIME_HTML.format(datetime.now())


if __name__ == "__main__":
    # Launch the Flask dev server
    app.run(host="0.0.0.0", port=5002, debug=True)
