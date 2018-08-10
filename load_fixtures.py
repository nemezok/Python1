import db

fixtures_sql = '''
INSERT INTO catalog (title, descr, price, image) VALUES (
  "Супермясная",
  "Цыпленок, говядина (фарш), пикантная пепперони, томатный соус, острая чоризо, моцарелла и бекон",
  "395,545,755",
  "a.jpg"
);
INSERT INTO catalog (title, descr, price, image) VALUES (
  "Четыре сыра",
  "Сыр блючиз, томатный соус, моцарелла и смесь сыров чеддер и пармезан",
  "275,415,515",
  "b.jpg"
);
INSERT INTO catalog (title, descr, price, image) VALUES (
  "Мясная",
  "Цыпленок, ветчина, пикантная пепперони, томатный соус, острая чоризо и моцарелла",
  "275,415,515",
  "c.jpg"
);
INSERT INTO catalog (title, descr, price, image) VALUES (
  "Ветчина и грибы",
  "Ветчина, томатный соус, шампиньоны и моцарелла",
  "275,415,515",
  "d.jpg"
);
INSERT INTO catalog (title, descr, price, image) VALUES (
  "Маргарита",
  "Томатный соус, моцарелла, томаты и орегано",
  "275,415,515",
  "e.jpg"
);
INSERT INTO catalog (title, descr, price, image) VALUES (
  "Четыре сезона",
  "Ветчина, пикантная пепперони, томатный соус, кубики брынзы, шампиньоны, моцарелла, томаты и орегано",
  "275,415,515",
  "f.jpg"
);
'''


def run():
    conn, cur = db.get_db()
    cur.executescript(fixtures_sql)
    conn.commit()

if __name__ == '__main__':
    run()
