from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

# Step 2: Read the JSON file
with open('blog_posts.json', 'r') as file:
    blog_posts = json.load(file)


@app.route('/')
def index():
    # Step 4: Pass the data to the template
    return render_template('index.html', posts=blog_posts)


def get_next_id():
    if not blog_posts:
        return 1
    max_id = max(post['id'] for post in blog_posts)
    return max_id + 1


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        content = request.form.get('content')
        new_post = {
            'id': get_next_id(),  # Generate the next ID
            'title': title,
            'author': author,
            'content': content
        }
        blog_posts.append(new_post)
        with open('blog_posts.json', 'w') as file:
            json.dump(blog_posts, file)
        return redirect(url_for('index'))
    return render_template('add.html')


@app.route('/delete/<int:post_id>')
def delete(post_id):
    global blog_posts
    blog_posts = [post for post in blog_posts if post['id'] != post_id]
    with open('blog_posts.json', 'w') as file:
        json.dump(blog_posts, file)
    return redirect(url_for('index'))


def fetch_post_by_id(post_id):
    for post in blog_posts:
        if post['id'] == post_id:
            return post
    return None


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    post = fetch_post_by_id(post_id)
    if post is None:
        return "Post not found", 404

    if request.method == 'POST':
        post['title'] = request.form.get('title')
        post['author'] = request.form.get('author')
        post['content'] = request.form.get('content')
        with open('blog_posts.json', 'w') as file:
            json.dump(blog_posts, file)
        return redirect(url_for('index'))

    return render_template('update.html', post=post)


if __name__ == '__main__':
    app.run()