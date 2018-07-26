import datetime
import sqlite3


def get_db():
    conn = sqlite3.connect('blog.db')
    cur = conn.cursor()
    return conn, cur


def get_topics():
    conn, cur = get_db()

    topic_rows = cur.execute(
        'SELECT id, name FROM topic'
    ).fetchall()

    # Returns:
    # [
    #   (1, 'Управление'),
    #   (2, 'Развитие'),
    #   (3, 'Природа'),
    #   (4, 'Спорт')
    # ]

    topics = []
    for topic_row in topic_rows:
        topic = {
            "id": topic_row[0],
            "name": topic_row[1],
        }

        topics.append(topic)
    return topics


def get_topic(topic_id):
    conn, cur = get_db()

    topic_row = cur.execute('SELECT id, name FROM topic WHERE id = ?', [topic_id]).fetchone()

    # Returns:
    # (1, 'Управление')

    topic = {
        "id": topic_row[0],
        "name": topic_row[1],
    }

    return topic


def update_topic(topic_id, new_name):
    conn, cur = get_db()

    cur.execute('UPDATE topic SET name = ? WHERE id = ?', [new_name, topic_id])

    conn.commit()


def add_topic(topic_name):
    conn, cur = get_db()

    cur.execute(
        'INSERT INTO topic (name) VALUES (?)', [topic_name]
    )

    conn.commit()


def get_posts():
    conn, cur = get_db()

    post_rows = cur.execute(
        'SELECT id, topic_id, created, author, title, body FROM post ORDER BY created DESC'
    ).fetchall()

    posts = []
    for post_row in post_rows:
        topic_id = post_row[1]
        topic = get_topic(topic_id)
        post = {
            "id": post_row[0],
            "topic_id": topic_id,
            "topic": topic['name'],
            "created": post_row[2],
            "author": post_row[3],
            "title": post_row[4],
            "body": post_row[5]
        }

        posts.append(post)
    return posts


def get_posts_by_author(author):
    conn, cur = get_db()

    posts_sql = 'SELECT id, topic_id, created, author, title, body FROM post WHERE author = ? ORDER BY created DESC'
    post_rows = cur.execute(posts_sql, [author]).fetchall()

    posts = []
    for post_row in post_rows:
        topic_id = post_row[1]
        topic = get_topic(topic_id)
        post = {
            "id": post_row[0],
            "topic_id": topic_id,
            "topic": topic['name'],
            "created": post_row[2],
            "author": post_row[3],
            "title": post_row[4],
            "body": post_row[5]
        }
        posts.append(post)
    return posts


def add_post(topic_id, author, title, body):
    conn, cur = get_db()

    cur.execute(
        'INSERT INTO post (topic_id, created, author, title, body) VALUES (?, ?, ?, ?, ?)',
        [topic_id, datetime.datetime.now(), author, title, body]
    )
    conn.commit()


if __name__ == '__main__':
    import init_db
    import load_fixtures
    init_db.run()
    load_fixtures.run()

    topics = get_topics()

    posts = get_posts()
    print('Fixtures posts:')
    for post in posts:
        print(post)

    add_post(topic='Природа', author='andrey', title='title', body='body')

    posts = get_posts()
    print('With added post:')
    for post in posts:
        print(post)

    posts = get_posts_by_author('andrey')
    print('By author posts:')
    for post in posts:
        print(post)
