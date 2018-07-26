import db

fixtures_sql = '''
INSERT INTO topic (id, name) VALUES (1, "Управление");
INSERT INTO topic (id, name) VALUES (2, "Развитие");
INSERT INTO topic (id, name) VALUES (3, "Природа");
INSERT INTO topic (id, name) VALUES (4, "Спорт");

INSERT INTO post (id, topic_id, created, author, title, body) VALUES (
  1, 1, "2018-06-13 13:00:00", "andrey", "Задача организации", "Задача организации, в особенности же новая модель организационной деятельности"
);
INSERT INTO post (id, topic_id, created, author, title, body) VALUES (
  2, 2, "2018-06-13 19:45:43", "alexey", "Модернизация модели развития", "Разнообразный и богатый опыт постоянный количественный рост и сфера нашей"
);
'''


def run():
    conn, cur = db.get_db()
    cur.executescript(fixtures_sql)
    conn.commit()

if __name__ == '__main__':
    run()
