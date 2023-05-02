from flask import Flask, render_template, request, jsonify
from database import load_comments_from_db, add_comments_to_db, add_contact_to_db

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/posts', methods=['get', 'post'])
def posts():
    comments = load_comments_from_db()
    data= request.form
    return render_template('first_blog.html', data=data, comments=comments)


@app.route('/api/posts')
def list_comments():
    comments = load_comments_from_db()
    return jsonify(comments)


@app.route('/posts/new_comment', methods=['post'])
def comment():
    data = request.form
    add_comments_to_db(data)
    comments = load_comments_from_db()
    return render_template('first_blog.html', data=data, comments=comments)


@app.route('/contact/new', methods=['post'])
def new_contact():
    data = request.form
    add_contact_to_db(data)
    return render_template('contact.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)