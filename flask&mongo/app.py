from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson import ObjectId


app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['items']

# Define routes
@app.route('/')
def index():
    items = collection.find()
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add_item():
    name = request.form['name']
    description = request.form['description']
    collection.insert_one({'name': name, 'description': description})
    return redirect(url_for('index'))

@app.route('/edit/<item_id>', methods=['POST'])
def edit_item(item_id):
    name = request.form['name']
    description = request.form['description']
    collection.update_one({'_id': ObjectId(item_id)}, {'$set': {'name': name, 'description': description}})
    return redirect(url_for('index'))

@app.route('/delete/<item_id>')
def delete_item(item_id):
    collection.delete_one({'_id': ObjectId(item_id)})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
