from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

with open('blog_posts.json', 'r') as file:
    blog_posts = json.load(file)


@app.route('/')
def index():
    return render_template('index.html', posts=blog_posts)


def get_next_id():
    return max((post['id'] for post in blog_posts), default=0) + 1


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_post = {
            'id': get_next_id(),
            'title': request.form.get('title'),
            'author': request.form.get('author'),
            'content': request.form.get('content'),
            'likes': 0
        }
        blog_posts.append(new_post)
        with open('blog_posts.json', 'w') as file:
            json.dump(blog_posts, file)
        return redirect(url_for('index'))
    return render_template('add.html')


@app.route('/delete/<int:post_id>')
def delete(post_id):
    global blog_posts
    updated_blog_posts = []
    for post in blog_posts:
        if post['id'] != post_id:
            updated_blog_posts.append(post)
    blog_posts = updated_blog_posts
    with open('blog_posts.json', 'w') as file:
        json.dump(blog_posts, file)
    return redirect(url_for('index'))

# alternative to delete
# @app.route('/delete/<int:post_id>')
# def delete(post_id):
#     global blog_posts
#     for i, post in enumerate(blog_posts):
#         if post['id'] == post_id:
#             blog_posts.pop(i)
#             break
#     with open('blog_posts.json', 'w') as file:
#         json.dump(blog_posts, file)
#     return redirect(url_for('index'))


def fetch_post_by_id(post_id):
    for post in blog_posts:
        if post['id'] == post_id:
            return post
    return None


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    post = fetch_post_by_id(post_id)
    
    if not post:
        return "The blog post was not found", 404
    
    if request.method == 'POST':
        post.update({
            'title': request.form.get('title'),
            'author': request.form.get('author'),
            'content': request.form.get('content')
        })
        
        with open('blog_posts.json', 'w') as file:
            json.dump(blog_posts, file)
        return redirect(url_for('index'))
    return render_template('update.html', post=post)


@app.route('/like/<int:post_id>', methods=['POST'])
def like(post_id):
    post = fetch_post_by_id(post_id)
    if not post:
        return "The blog post was not found", 404
    post['likes'] += 1
    with open('blog_posts.json', 'w') as file:
        json.dump(blog_posts, file)
    return redirect(url_for('index'))


@app.route('/dislike/<int:post_id>', methods=['POST'])
def dislike(post_id):
    post = fetch_post_by_id(post_id)
    if not post:
        return "The blog post was not found", 404
    if post['likes'] > 0:
        post['likes'] -= 1
    with open('blog_posts.json', 'w') as file:
        json.dump(blog_posts, file)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
