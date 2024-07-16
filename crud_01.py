from flask import request

@app.route('/update_profile', methods=['POST'])
def update_profile():
    username = request.form['username']
    email = request.form['email']

    # Update the user's profile with the new data
    return f"Updating profile of {username} with email {email}"