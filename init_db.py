import db

schema_sql = '''
DROP TABLE IF EXISTS topic;
DROP TABLE IF EXISTS post;

CREATE TABLE topic (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT UNIQUE NOT NULL
);

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  topic_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL,
  author TEXT NOT NULL,
  title TEXT NOT NULL,
  body TEXT NOT NULL
);
'''


def run():
    conn, cur = db.get_db()
    cur.executescript(schema_sql)


if __name__ == '__main__':
    run()
