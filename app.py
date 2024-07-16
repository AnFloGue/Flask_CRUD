from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

users = {
    'Alice': {'age': 25, 'country': 'USA'},
    'Bob': {'age': 30, 'country': 'UK'},
    'Charlie': {'age': 35, 'country': 'Australia'}
}
animal_data = {
    "Name": "Fox",
    "Color": "Black",
}


@app.route('/update-profile', methods=['GET', 'POST'])
def update_profile():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        # Add logic to update user profile here
        return f"Updating profile of {username} with email {email}"
    else:
        return render_template('update-profile.html')


@app.route('/update-country', methods=['GET', 'POST'])
def update_country():
    if request.method == 'POST':
        name = request.form.get('name')
        country = request.form.get('country')
        if name in users:
            users[name]['country'] = country
            for user, details in users.items():
                print(f"{user} is {details['age']} years old from {details['country']}")
        else:
            print(f"User {name} not found.")
        
        return redirect(url_for('update_country_success'))
    return render_template('update-country.html')


@app.route('/update-country-success')
def update_country_success():
    for user, details in users.items():
        print(f"{user} is {details['age']} years old from {details['country']}")
    return 'Country update successful!'


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/all-users')
def all_users():
    return render_template('all-users.html', users=users)


@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'Guest')
    return render_template('greet.html', title=name, user='Alice', time=datetime.now(), users=users)


@app.route('/')
def index():
    return render_template('index.html', title='Home', user='Alice', time=datetime.now(), users=users)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500


@app.route('/animal-info')
def animal_info():
    return render_template('animal.html', animal_data=animal_data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
