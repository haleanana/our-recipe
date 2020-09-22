import os
import datetime
from flask import Flask, render_template, redirect, request, url_for, abort
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
    return render_template("index.html", recipes=mongo.db.recipes.find())


@app.route('/get_recipes')
def get_recipes():
	return render_template("recipes.html", recipes=mongo.db.recipes.find().sort('added_on', -1))

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
    recipe = request.form.to_dict()
    added_on = now.strftime('%d %B %Y')
    recipe['added_on'] = added_on
    mongo.db.recipes.insert_one(recipe)
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
    'url_image': request.form.get('url_image'),
    'last_update': now.strftime('%d %B %Y'),

    })

    return redirect(url_for('get_recipes'))

@app.route('/favourites/<recipe_id>', methods = ['POST'])
def add_to_favourites(recipe_id):
    mongo.db.recipes.update({'_id': ObjectId(recipe_id)},
    {'$set' : {'fave': 'Yes'}
    })
    return render_template('favourites.html', recipes = mongo.db.recipes.find())

@app.route('/show_favourites')
def show_favourites():
    return render_template('favourites.html', recipes = mongo.db.recipes.find())

@app.route('/search', methods = ['POST', 'GET'])
def search():
    mongo.db.recipes.create_index([('$**', 'text')])
    query = request.form.get("query")
    result = mongo.db.recipes.find({"$text": {"$search": query}}).limit(10)
    result_count = mongo.db.recipes.find({"$text": {"$search": query}}).count()

    if result_count == 0:
       return render_template("no_results.html", result=result, query=query, message = "No results found. Please try again")

    else:
        return render_template( "query_results.html", result=result, query=query )


@ app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html')

@ app.errorhandler(500)
def internal_server(error):
    return render_template('errors/500.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(
        os.environ.get('PORT')),
        debug=True)

