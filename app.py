import datetime

from flask import (Flask, request, render_template,
                   redirect, url_for, flash)
import db

app = Flask(__name__)
app.secret_key = b'simbirsoft73(*&13%*$&^#'


@app.route('/')
def index():
    posts = db.get_posts()
    return render_template('posts.html', posts=posts)


@app.route('/add_post', methods=['POST', 'GET'])
def add_post():
    if request.method == 'POST':

        db.add_post(topic_id=request.form['topic_id'],
                    author=request.form['author'],
                    title=request.form['title'],
                    body=request.form['body'])

        flash('Новый пост добавлен')

        return redirect(url_for('index'))
    else:
        topics = db.get_topics()
        return render_template('add_post.html', topics=topics)


@app.route('/author/<string:author>')
def author(author):
    author_posts = db.get_posts_by_author(author)

    return render_template('author.html',
                           author=author,
                           posts=author_posts)


@app.route('/topics')
def topics():
    topics = db.get_topics()

    return render_template('topics.html',
                           topics=topics)


@app.route('/topics/<int:topic_id>', methods=['POST', 'GET'])
def topic(topic_id):
    topic = db.get_topic(topic_id)

    if request.method == 'POST':
        topic_id = request.form['topic_id']
        new_topic_name = request.form['topic_name']
        db.update_topic(topic_id, new_topic_name)

        flash('Тема "{0}" теперь называется "{1}"'.format(topic['name'], new_topic_name))

        return redirect(url_for('topics'))

    return render_template('topic.html',
                           topic=topic)


@app.route("/about")
def about():
    return render_template('about.html')
