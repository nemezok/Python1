import db
import datetime
from flask import (flash, session)

def list (items = None):
    conn, cur = db.get_db()
    result = []

    r = []
    r.append('SELECT * FROM catalog')
    if not items is None:
        if items:
            r.append('WHERE ID IN ({0})'.format(items))
        else:
            return result
    r = ' '.join(r)
    rows = cur.execute(r).fetchall()

    for row in rows:
        pizza = {
            'ID': row[0],
            'title': row[1],
            'descr': row[2],
            'price': row[3].split(','),
            'image': 'img/pizza/'+row[4]
        }
        result.append(pizza)

    return result

def cart_init ():
    if 'cart' not in session:
        session['cart'] = []
        session.modified = True

def addtocart (data):
    cart_init()

    if(data['pizza_id'] not in session['cart']):
        session['cart'].append(data['pizza_id'])
        session.modified = True
        flash('Товар добавлен в корзину')

    return 'success'

def removefromcart (data):
    del session['cart'][session['cart'].index(data['pizza_id'])]
    session.modified = True
    flash('Товар удален из корзины')
    return 'success'

def get_orders ():
    conn, cur = db.get_db()
    rows = cur.execute(
        'SELECT * FROM orders ORDER BY ID'
    ).fetchall()

    data = []
    for row in rows:
        itemlist = list(row[4])
        summprice = 0.00
        for p in itemlist:
            summprice += float(p['price'][0])

        summprice = format(summprice, '.2f')

        data.append({
            'ID': row[0],
            'fio': row[1],
            'phone': row[2],
            'address': row[3],
            'itemlist': itemlist,
            'time': row[5],
            'status': row[6],
            'summprice': summprice
        })

    data.reverse()
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
    flash('Ваш заказ принят')
    return ''

def orderstatus(data):
    conn, cur = db.get_db()
    cur.execute(
        'UPDATE orders SET status = ? WHERE ID = ?',
        [data['status'], data['order_id']]
    )
    conn.commit()
    return ''

def statuslist ():
    return {0:'Новый', 1:'Отправлен на кухню', 2:'Отправлен в доставку', 3:'Доставлен'}

if __name__ == '__main__':
    qwe = 1+5
    print(qwe)
    #del (session['cart'])
    #session.clear()