import db
import datetime
from flask import (flash, session)

def cart_init ():
    if 'cart' not in session:
        session['cart'] = []
        session.modified = True

def addtocart (data):
    #del (session['cart'])
    #session.clear()
    cart_init()

    if(data['pizza_id'] not in session['cart']):
        session['cart'].append(data['pizza_id'])
        session.modified = True

    return 'success'

def removefromcart (data):
    del session['cart'][session['cart'].index(data['pizza_id'])]
    session.modified = True
    return 'success'

def get_orders ():
    conn, cur = db.get_db()
    rows = cur.execute(
        'SELECT * FROM orders'
    ).fetchall()

    data = []
    for row in rows:
        data.append({
            'ID': row[0],
            'fio': row[1],
            'phone': row[2],
            'address': row[3],
            'itemlist': list(row[4]),
            'time': row[5],
        })

    return data

def addorder (data):
    conn, cur = db.get_db()
    items = ','.join(session['cart'])
    cur.execute(
        'INSERT INTO orders (fio, phone, address, items, time) VALUES (?, ?, ?, ?, ?)',
        [data['fio'], data['phone'], data['address'], items, datetime.datetime.now()]
    )
    conn.commit()
    del session['cart']
    session.modified = True
    flash('Ваш заказ успешно оформлен')
    return ''


if __name__ == '__main__':
    #from flask import session
    #if 'cart' not in session:
    #    session['cart'] = []

    #session['cart'].append(['ThePizza'])
    #session.modified = True
    qwe = 1+5
    print(qwe)
    #print(session)
    #print(session.cart)