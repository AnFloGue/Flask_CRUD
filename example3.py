from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

HELLO_HTML = """
    <html><body>
        <h1>Hello, {0}!</h1>
        The time is {1}.
    </body></html>"""


@app.route('/')
def hello():
    if 'name' in request.args:
        name = request.args['name']
    else:
        name = 'friend'
    return HELLO_HTML.format(name, str(datetime.now()))


if __name__ == "__main__":
    # Launch the Flask dev server
    app.run(host="0.0.0.0", port=5003, debug=True)
