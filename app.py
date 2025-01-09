import os
from flask import Flask, render_template, redirect, request, url_for, jsonify, flash, session
from flask_session import Session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bson.json_util import dumps
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf.csrf import CSRFProtect
from wtforms import Form, StringField, PasswordField, validators
from os import path

# Import environment variables (if available)
if path.exists("env.py"):
    import env

# Create Flask app instance
app = Flask(name)

# Flask configurations
app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]
app.config["MONGO_URI"] = os.environ["MONGODB_URI"]
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Enable CSRF protection
csrf = CSRFProtect(app)

# MongoDB instance
mongo = PyMongo(app)

# Form validation classes
class RegisterForm(Form):
    username = StringField('Username', [validators.Length(min=3, max=25), validators.DataRequired()])
    email = StringField('Email', [validators.Email(), validators.DataRequired()])
    password = PasswordField('Password', [validators.Length(min=5, max=10), validators.DataRequired()])

class LoginForm(Form):
    email = StringField('Email', [validators.Email(), validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])

class ItemForm(Form):
    item_name = StringField('Item Name', [validators.DataRequired()])
    item_category = StringField('Category', [validators.DataRequired()])
    item_description = StringField('Description', [validators.DataRequired()])
    item_location = StringField('Location', [validators.DataRequired()])
    item_img = StringField('Image URL', [validators.Optional()])

# Routes

@app.route('/')
def home():
    """Display all items"""
    search_query = request.args.get('search', '')
    if search_query:
        items = mongo.db.items.find({
            "$or": [
                {"item_name": {"$regex": search_query, "$options": "i"}},
                {"item_description": {"$regex": search_query, "$options": "i"}}
            ]
        })
    else:
        items = mongo.db.items.find()
    return render_template(
        '/pages/home.html', 
        items=items,
        active='home',
        title="Re-Use Gang"
    )


@app.route('/register', methods=['POST', 'GET'])
def register():
    """Register a new user"""
    form = RegisterForm(request.form)
    if request.method == "POST" and form.validate():
        users = mongo.db.users
        used_name = users.find_one({'username': form.username.data})
        used_email = users.find_one({'email': form.email.data})
        if not used_name and not used_email:
            hashed_pwd = generate_password_hash(form.password.data)
            users.insert_one({
                "username": form.username.data,
                "email": form.email.data,
                "password": hashed_pwd
            })
            session['username'] = form.username.data
            flash(f"Welcome to the Gang, {session['username']}!")
            return redirect(url_for('home'))
        else:
            flash("Username or email is already in use. Please try again.")
            return redirect(url_for('register'))
    return render_template('/components/register.html', form=form, active='register')


@app.route('/login', methods=['POST', 'GET'])
def login():
    """Log in a user"""
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        users = mongo.db.users
        matched_user = users.find_one({'email': form.email.data})
        if matched_user and check_password_hash(matched_user["password"], form.password.data):
            session['username'] = matched_user["username"]
            flash(f"Welcome back, {session['username']}!")
            return redirect(url_for('home'))
        else:
            flash("Invalid login credentials. Please try again.")
            return redirect(url_for('login'))
    return render_template('/components/login.html', form=form, active='login')

@app.route('/logout')
def logout():
    """Log out the user"""
    session.clear()
    flash("You have been logged out!")
    return redirect(url_for('home'))


@app.route('/account', methods=["GET"])
def account():
    """Display the user's account page"""
    if "username" not in session:
        flash("Please log in to access your account.")
        return redirect(url_for('login'))
    user_items = mongo.db.items.find({'username': session['username']})
    return render_template('/pages/account.html', items=user_items, active='account')


@app.route('/items/filter', methods=["POST"])
def filter_items():
    """Filter items by category"""
    cat = request.get_json()
    if cat == 'default':
        all_items = mongo.db.items.find()
        return dumps(all_items)
    else:
        found_items = mongo.db.items.find({'item_category': cat})
        return dumps(found_items)


@app.route('/items/add', methods=["POST", "GET"])
def add_item():
    """Add a new item"""
    form = ItemForm(request.form)
    categories = ["Kids", "Outdoor", "Household", "Other"]
    if request.method == "POST" and form.validate():
        if "username" in session:
            items = mongo.db.items
            item_owner = mongo.db.users.find_one({'username': session['username']})
            items.insert_one({
                'username': session['username'],
                'item_contact': item_owner['email'],
                'item_name': form.item_name.data,
                'item_category': form.item_category.data,
                'item_description': form.item_description.data,
                'item_location': form.item_location.data,
                'item_img': form.item_img.data
            })
            flash("Your item has been added successfully!")
            return redirect(url_for('home'))
        else:
            flash("Please log in to add items.")
            return redirect(url_for('login'))
    return render_template('/pages/additem.html', categories=categories, form=form, active='additem')


@app.route('/items/update/<item_id>', methods=["POST", "GET"])
def update_item(item_id):
    """Update an existing item"""
    form = ItemForm(request.form)
    if "username" not in session:
        flash("Please log in to edit items.")
        return redirect(url_for('login'))
    clicked_item = mongo.db.items.find_one({'_id': ObjectId(item_id)})
    if request.method == "POST" and form.validate():
        mongo.db.items.update_one({'_id': ObjectId(item_id)}, {"$set": {
            'item_name': form.item_name.data,
            'item_category': form.item_category.data,
            'item_description': form.item_description.data,
            'item_location': form.item_location.data,
            'item_img': form.item_img.data
        }})
        flash("Your item has been updated successfully!")
        return redirect(url_for('account'))
    return render_template('/pages/updateitem.html', item=clicked_item, form=form, active='edit')


@app.route('/items/delete/<item_id>', methods=["POST"])
def delete_item(item_id):
    """Delete an item"""
    mongo.db.items.delete_one({'_id': ObjectId(item_id)})
    flash("Your item has been deleted.")
    return redirect(url_for('account'))


# Error Handlers
@app.errorhandler(404)
def not_found(error):
    return render_template("/pages/404.html", error=error), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template("/pages/500.html", error=error), 500


if name == "main":
    app.run(host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", "5000")), debug=False)
    
