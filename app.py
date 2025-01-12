from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_pymongo import PyMongo
from wtforms import Form, StringField, PasswordField, validators
from email_validator import validate_email, EmailNotValidError

app = Flask(__name__)
app.secret_key = 'polya1606'

# MongoDB Configuration
app.config["MONGO_URI"] = "mongodb://localhost:27017/give-take"  # Replace with your database name
mongo = PyMongo(app)

# WTForms for Login and Register
class LoginForm(Form):
    email = StringField('Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [validators.DataRequired()])

class RegisterForm(Form):
    username = StringField('Username', [validators.DataRequired()])
    email = StringField('Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [validators.DataRequired()])

# Home Route
@app.route('/')
def home():
    search_query = request.args.get('search', '')
    category_filter = request.args.get('item_category')
    items = list(mongo.db.items.find())

    # Apply search and category filters if provided
    if search_query:
        items = [item for item in items if search_query.lower() in item['item_name'].lower()]
    if category_filter and category_filter != 'default':
        items = [item for item in items if item['item_category'] == category_filter]

    return render_template('pages/home.html', items=items)

# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        email = form.email.data
        password = form.password.data
        user = mongo.db.users.find_one({'email': email})

        if user and user['password'] == password:
            session['username'] = user['username']
            flash('Logged in successfully!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid credentials. Please try again.', 'danger')

    return render_template('components/login.html', form=form)

# Register Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        if mongo.db.users.find_one({'email': email}):
            flash('Email already registered.', 'danger')
        else:
            mongo.db.users.insert_one({'username': username, 'email': email, 'password': password})
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))

    return render_template('components/register.html', form=form)

# Account Route
@app.route('/account')
def account():
    if 'username' not in session:
        flash('Please log in to access your account.', 'danger')
        return redirect(url_for('login'))

    username = session['username']
    user_items = list(mongo.db.items.find({'username': username}))

    return render_template('pages/account.html', items=user_items, active='account')

# Add Item Route
@app.route('/items/add', methods=['GET', 'POST'])
def add_item():
    if 'username' not in session:
        flash('Please log in to add items.', 'danger')
        return redirect(url_for('login'))

    if request.method == 'POST':
        item_data = {
            'item_name': request.form['item_name'],
            'item_category': request.form['item_category'],
            'item_description': request.form['item_description'],
            'item_location': request.form['item_location'],
            'item_img': request.form['item_img'],
            'username': session['username']
        }
        mongo.db.items.insert_one(item_data)
        flash('Item added successfully!', 'success')
        return redirect(url_for('home'))

    categories = ['Kids', 'Outdoor', 'Household', 'Other']
    return render_template('pages/additem.html', categories=categories)

# Update Item Route
@app.route('/items/update/<item_id>', methods=['GET', 'POST'])
def update_item(item_id):
    if 'username' not in session:
        flash('Please log in to update items.', 'danger')
        return redirect(url_for('login'))

    item = mongo.db.items.find_one({'_id': item_id})
    if not item:
        flash('Item not found.', 'danger')
        return redirect(url_for('account'))

    if request.method == 'POST':
        updated_data = {
            'item_name': request.form['item_name'],
            'item_category': request.form['item_category'],
            'item_description': request.form['item_description'],
            'item_location': request.form['item_location'],
            'item_img': request.form['item_img']
        }
        mongo.db.items.update_one({'_id': item_id}, {'$set': updated_data})
        flash('Item updated successfully!', 'success')
        return redirect(url_for('account'))

    return render_template('pages/updateitem.html', item=item)

# Delete Item Route
@app.route('/items/delete/<item_id>', methods=['POST'])
def delete_item(item_id):
    if 'username' not in session:
        flash('Please log in to delete items.', 'danger')
        return redirect(url_for('login'))

    mongo.db.items.delete_one({'_id': item_id})
    flash('Item archived successfully.', 'success')
    return redirect(url_for('account'))

# Logout Route
@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))

# Custom Error Pages
@app.errorhandler(404)
def not_found(error):
    return render_template('pages/404.html'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('pages/500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)