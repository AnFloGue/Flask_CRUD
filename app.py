from flask import Flask, render_template
import json

app = Flask(__name__)

# Step 2: Read the JSON file
with open('blog_posts.json', 'r') as file:
    blog_posts = json.load(file)


@app.route('/')
def index():
    # Step 4: Pass the data to the template
    return render_template('index.html', posts=blog_posts)


if __name__ == '__main__':
    app.run()
