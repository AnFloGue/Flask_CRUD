from flask import Flask, request

app = Flask(__name__)

HOME_HTML = """
    <html><body>
        <h2>Welcome to the Greeter</h2>
        <form action="/greet">
            What's your name? <input type='text' name='username'><br>
            What's your favorite food? <input type='text' name='favfood'><br>
            <input type='submit' value='Continue'>
        </form>
    </body></html>"""

GREET_HTML = """
    <html><body>
        <h2>Hello, {0}!</h2>
        {1}
    </body></html>
    """

@app.route('/')
def home():
    return HOME_HTML


@app.route('/greet')
def greet():
    username = request.args.get('username', '')
    favfood = request.args.get('favfood', '')
    if username == '':
        username = 'World'
    if favfood == '':
        msg = 'You did not tell me your favorite food.'
    else:
        msg = f'I like {favfood}, too.'
    
    return GREET_HTML.format(username, msg)


if __name__ == "__main__":
    # Launch the Flask dev server
    app.run(host="0.0.0.0", port=5004, debug=True)
