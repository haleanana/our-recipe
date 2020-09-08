import os
import datetime
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

from os import path
if path.exists('env.py'):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get('MONGO_DB')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)
now = datetime.datetime.now()

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/get_recipes')
def get_recipes():
	return render_template("recipes.html", recipes=mongo.db.recipes.find())

@app.route('/show_recipe/<recipe_id>')
def show_recipe(recipe_id):
    my_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    return render_template('showrecipe.html', recipe= my_recipe, categories = all_categories)

@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html", categories= mongo.db.categories.find())

@app.route('/insert_recipe', methods =['POST'])
def insert_recipe():
    mongo.db.recipes.insert_one(request.form.to_dict())
    if 'recipe_image' in request.files:
        recipe_image = request.file['recipe_image']
        mongo.save_file(recipe_image.filename, recipe_image)
        mongo.db.recipes.insert_one({'recipe_image_name':recipe_image})
    return redirect(url_for('get_recipes'))

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    my_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    return render_template('editrecipe.html', recipe= my_recipe, categories = all_categories)

@app.route('/update_recipe/<recipe_id>', methods = ['POST'])
def update_recipe(recipe_id):
    mongo.db.recipes.update({'_id': ObjectId(recipe_id)},
    {'recipe_name': request.form.get('recipe_name'),
    'category_name': request.form.get('category_name'),
    'recipe_description': request.form.get('recipe_description'),
    'ingredients': request.form.get('ingredients'),
    'methods': request.form.get('methods'),
    'prep_time': request.form.get('prep_time'), 
    'cooking_time': request.form.get('cooking_time'),
    'last_update': now.strftime('%d %B %Y') 
    })

    return redirect(url_for('get_recipes'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(
        os.environ.get('PORT')),
        debug=True)

