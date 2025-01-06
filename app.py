import os
from flask import Flask, render_template, redirect, request, url_for, jsonify, flash, session, Response
from flask_session import Session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bson.json_util import dumps
from werkzeug.security import generate_password_hash, check_password_hash

from os import path
# import file where username and password of MongoDB is saved
if path.exists("env.py"):
    import env

# create instance of flask
app = Flask(__name__)  

# add configuration to Flask app
app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]
app.config["MONGODB_NAME"] = "reuse-gang"
app.config["MONGO_URI"] = os.environ["MONGODB_URI"]

# create an instance of Pymongo with app object being pushed as argument
mongo = PyMongo(app)


@app.route('/')
def home():
    '''Show all items stored and found from MongoDB collection items'''
    return render_template(
        '/pages/home.html', 
        items=mongo.db.items.find(),
        users=mongo.db.users.find(), 
        active='home',
        title="Re-Use Gang")


@app.route('/register', methods=['POST', 'GET'])
def register():
    '''Render register modal if method is get and after form is submitted by user,
    this function will check if username or email address are already used and if not,
    will hash password before sending all new user data to db'''
    if request.method == "POST":
        users = mongo.db.users
        used_name = users.find_one({'username': request.form["username"]})
        used_email = users.find_one({'email': request.form["email"]})
        if (used_email or used_name) is None:
            user_pwd = generate_password_hash(request.form["password"])
            users.insert_one({
                "username": request.form["username"],
                "email": request.form["email"], 
                "password": user_pwd
                })
            session['username'] = request.form["username"]
            flash("Welcome to the Gang, " + session['username'] + "!")
            return redirect(url_for('home'))
        elif used_name is not None:
            flash("This username already exists, please choose another one")
            return redirect(url_for('register'))
        else:
            flash("This email address is already registered, would you like to log in instead?")
            return redirect(url_for('login'))
    return render_template(
        '/components/register.html',
        active='register'
        )


@app.route('/login', methods=['POST', 'GET'])
def login():
    '''Render login modal if method is get and after form is submitted by user,
    this function will find user associated with email address, compare password
    submitted with password associated with user. Then will redirect to home'''
    if request.method == "POST":
        users = mongo.db.users
        matched_user = users.find_one({'email': request.form["email"]})
        if matched_user:
            if check_password_hash(matched_user["password"], request.form["password"]):
                flash("Welcome back " + matched_user["username"])
                session['username'] = matched_user["username"]
                return redirect(url_for('home'))
            else:
                flash("You've entered the wrong password")
                return redirect(url_for('login'))
        else:
            flash("This email address is unknown to our records.")
            return redirect(url_for('login'))
    return render_template(
        '/components/login.html',
        active='login'
        )


@app.route('/logout', methods=['POST', 'GET'])
def logout():
    '''remove the username from the session if it's there'''
    [session.pop(key) for key in list(session.keys())]
    flash('You have successfully logged out!')
    return redirect(url_for('home'))


@app.route('/account', methods=["POST", "GET"])
def account():
    '''If username is not in session, redirect to login.
    Else function will search all items associated
    with session username and render account template'''
    if "username" not in session:
        return redirect(url_for('login'))
    else:
        user_items = mongo.db.items.find({'username': session['username']})
        return render_template(
            '/pages/account.html', 
            items=user_items,
            active='account'
            )


@app.route('/items/filter', methods=["POST", "GET"])
def filter_items():
    '''JS received data from filter drop down menu and send it as json to this route.
    Function search all items under that category and return them as cursor object.
    Using dumps method from bson, send back response to JS which handles rendering 
    filtered data'''
    cat = request.get_json()
    if cat == 'default':
        all_items = mongo.db.items.find()
        return dumps(all_items)
    else:
        found_items = mongo.db.items.find({'item_category': cat})
        return dumps(found_items)


@app.route('/items/add', methods=["POST", "GET"])
def add_item():
    '''Create array of categories to display on template and add item form in html
    If username not in session, redirect to login.
    Render add item modal if method is get.
    After form is submitted by user, insert new item in db and redirect to home'''
    categories = ["Kids", "Outdoor", "Household", "Other"]

    if request.method == "POST":
        items = mongo.db.items
        item_owner = mongo.db.users.find_one({'username': session['username']})
        items.insert_one({
            'username': session['username'],
            'item_contact': item_owner['email'],
            'item_name': request.form['item_name'],
            'item_category': request.form['item_category'],
            'item_description': request.form['item_description'],
            'item_location': request.form['item_location'],
            'item_img': request.form['item_img']
        })
        flash("Thanks!Your free stuff will be shared immediately with the gang.")
        return redirect(url_for('home'))
    else:
        if "username" not in session:
            return redirect(url_for('login'))
        else:
            return render_template(
                '/pages/additem.html', 
                categories=categories,
                active='additem'
                )


@app.route('/items/update/<item_id>', methods=["POST", "GET"])
def update_item(item_id):
    '''If username not in session, redirect to login.
    Function finds associated item with objectID and render edit item modal if method is get.
    After form is submitted by user, update clicked_item in db and redirect to home'''
    if request.method == "POST":
        items = mongo.db.items
        item_owner = mongo.db.users.find_one({'username': session['username']})
        items.update({'_id': ObjectId(item_id)},
                     {
            'username': session['username'],
            'item_name': request.form.get('item_name'),
            'item_contact': item_owner['email'],
            'item_category': request.form.get('item_category'),
            'item_description': request.form.get('item_description'),
            'item_location': request.form.get('item_location'),
            'item_img': request.form.get('item_img')
            })
        flash("We've successfully updated your stuff.")
        return redirect(url_for('home'))
    else:
        clicked_item = mongo.db.items.find_one({'_id': ObjectId(item_id)})
        if "username" not in session:
            return redirect(url_for('login'))
        else:
            return render_template(
                '/pages/updateitem.html', 
                item=clicked_item,
                active='edit'
                )


@app.route('/items/delete/<item_id>', methods=["POST"])
def delete_item(item_id):
    '''find clicked item, loop through object and find item_name
    remove item and flash confirmation to user'''
    if request.method == "POST":
        item = mongo.db.items.find({'_id': ObjectId(item_id)})
        for i in item:
            item_name = i['item_name']
        mongo.db.items.remove({'_id': ObjectId(item_id)})
        flash(item_name + "has been deleted")
        return redirect(url_for('home'))


@app.errorhandler(500)
def internal_error(error):
    return render_template("/pages/500.html", error=error)


@app.errorhandler(404)
def not_found(error):
    return render_template("/pages/404.html", error=error)


if __name__ == "__main__":
    app.run(host=os.getenv("IP", "0.0.0.0"),
            port=int(os.getenv("PORT", "5000")),
            debug=False)
