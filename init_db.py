import db

schema_sql = '''
DROP TABLE IF EXISTS topic;
DROP TABLE IF EXISTS post;

DROP TABLE IF EXISTS catalog;
CREATE TABLE catalog (
  ID INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  descr TEXT NOT NULL,
  price TEXT NOT NULL,
  image TEXT NOT NULL
);

DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
  ID INTEGER PRIMARY KEY AUTOINCREMENT,
  fio TEXT NOT NULL,
  phone TEXT NOT NULL,
  address TEXT NOT NULL,
  items TEXT NOT NULL,
  time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  status INTEGER DEFAULT 0
);
'''

def run():
    conn, cur = db.get_db()
    cur.executescript(schema_sql)


if __name__ == '__main__':
    run()
