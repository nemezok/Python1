from flask import (Flask, request, render_template,
                   redirect, url_for, flash, session)
import datetime
import pizza

app = Flask(__name__)
app.secret_key = b'simbirsoft73(*&13%*$&^#'

@app.route('/')
def index():
    return render_template('index.html')

#@app.route('/author/<string:author>')
#def author(author):
    #author_posts = db.get_posts_by_author(author)
    #return render_template('author.html', author=author, posts=author_posts)

# КАТАЛОГ
@app.route('/catalog/', methods=['POST', 'GET'])
def catalog():
    if request.method == 'POST':
        pizza.addtocart(request.form)
        return redirect(url_for('catalog'))

    return render_template('catalog.html', catalog=pizza.list())

# КОРЗИНА
@app.route('/cart/', methods=['POST', 'GET'])
def cart():
    pizza.cart_init()
    if request.method == 'POST':
        if ('fio' in request.form):
            pizza.addorder(request.form)
            return redirect(url_for('cart'))
        if ('pizza_id' in request.form):
            pizza.removefromcart(request.form)
            return redirect(url_for('cart'))
    return render_template('cart.html', cart=pizza.list(','.join(session['cart'])))

# АДМИНКА
@app.route('/profile/', methods=['POST', 'GET'])
def profile():

    return render_template('admin.html')

# ЗАКАЗЫ
@app.route('/profile/orders/', methods=['POST', 'GET'])
def orders():
    if request.method == 'POST':
        if ('status' in request.form):
            pizza.orderstatus(request.form)
            return redirect(url_for('orders'))

    return render_template('orders.html', orders=pizza.get_orders(), statuslist=pizza.statuslist())

# Добавление\удаление товаров
@app.route('/profile/products/', methods=['POST', 'GET'])
def products():
    if request.method == 'POST':
        if ('status' in request.form):
            pizza.orderstatus(request.form)
            return redirect(url_for('orders'))

    return render_template('orders.html', orders=pizza.get_orders(), statuslist=pizza.statuslist())