import sqlite3

def get_db():
    conn = sqlite3.connect('blog.db')
    cur = conn.cursor()
    return conn, cur

if __name__ == '__main__':
    print('')
