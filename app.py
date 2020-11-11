import os
import datetime
from flask import Flask, render_template, redirect, request, url_for, flash, abort
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

from os import path
if path.exists('env.py'):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get('MONGO_DB')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)
now = datetime.datetime.now()

# Home
@app.route('/')
def home():
    return render_template("index.html", recipes = mongo.db.recipes.find().sort('added_on', -1).limit(3), views = mongo.db.recipes.find().sort('views', -1).limit(3))

# Shows all available recipes
@app.route('/recipes')
def recipes():
    query = request.args.get("query")
    if not query:
        recipes = mongo.db.recipes.find().sort('added_on', -1)
    else:
        #Finds the recipe using keywords the user enters
        mongo.db.recipes.create_index([('$**', 'text')])
        recipes = mongo.db.recipes.find({"$text":{"$search": query}}).limit(10)
    return render_template("recipes.html",  now = now.strftime('%d %B %Y'), recipes=recipes)

# Shows the selected recipes info
@app.route('/show_recipe/<recipe_id>')
def show_recipe(recipe_id):
    my_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    mongo.db.recipes.update(my_recipe,
    {'$inc' : {'views': 1}
    })
    return render_template('showrecipe.html', recipe= my_recipe, categories = all_categories)

# Returns the form to users for adding recipes
@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html", categories= mongo.db.categories.find())

# Adds the data from the form to my database
@app.route('/insert_recipe', methods =['POST'])
def insert_recipe():
    recipe = request.form.to_dict()
    added_on = now.strftime('%Y/%m/%d')
    recipe['added_on'] = added_on
    mongo.db.recipes.insert_one(recipe)
    return redirect(url_for('recipes'))
    
# Returns the form to users for updating recipes
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    my_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    return render_template('editrecipe.html', recipe= my_recipe, categories = all_categories)

# Updates the data when users submit
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
    'last_update': now.strftime('%Y/%m/%d'),

    })

    return redirect(url_for('recipes'))

# Shows all the recipe that has been favourited
@app.route('/show_favourites')
def show_favourites():
    return render_template('favourites.html', recipes = mongo.db.recipes.find())

# Adds the email entered to my database
@app.route('/sub', methods = ['POST'])
def sub():
    sub = request.form.to_dict()
    mongo.db.subscribers.insert(sub)
    flash("Thank you for subscribing.")
    return redirect(request.referrer)

@ app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html')

@ app.errorhandler(500)
def internal_server(error):
    return render_template('errors/500.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(
        os.environ.get('PORT')),
        debug=False)

