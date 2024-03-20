from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for initial testing
recipes = [
    {"id": 1, "title": "Spaghetti Carbonara", "ingredients": ["spaghetti", "eggs", "bacon", "parmesan cheese"], "instructions": "1. Cook spaghetti. 2. Fry bacon. 3. Mix eggs and cheese. 4. Combine all."},
    {"id": 2, "title": "Chocolate Chip Cookies", "ingredients": ["flour", "sugar", "butter", "chocolate chips"], "instructions": "1. Mix ingredients. 2. Bake at 350°F. 3. Enjoy!"}
]

ingredients = [
    {"id": 1, "name": "spaghetti"},
    {"id": 2, "name": "eggs"},
    {"id": 3, "name": "bacon"},
    {"id": 4, "name": "parmesan cheese"},
    {"id": 5, "name": "flour"},
    {"id": 6, "name": "sugar"},
    {"id": 7, "name": "butter"},
    {"id": 8, "name": "chocolate chips"}
]

# CRUD operations for recipes

# Read all recipes
@app.route('/recipes', methods=['GET'])
def get_recipes():
    return jsonify(recipes)

# Read one recipe by id
@app.route('/recipes/<int:id>', methods=['GET'])
def get_recipe(id):
    recipe = next((recipe for recipe in recipes if recipe['id'] == id), None)
    if recipe:
        return jsonify(recipe)
    else:
        return jsonify({"message": "Recipe not found"}), 

# Create a new recipe
@app.route('/recipes', methods=['POST'])
def create_recipe():
    data = request.json
    new_recipe = {
        "id": len(recipes) + 1,
        "title": data['title'],
        "ingredients": data['ingredients'],
        "instructions": data['instructions']
    }
    recipes.append(new_recipe)
    return jsonify(new_recipe), 

# Update a recipe
@app.route('/recipes/<int:id>', methods=['PUT'])
def update_recipe(id):
    recipe = next((recipe for recipe in recipes if recipe['id'] == id), None)
    if recipe:
        data = request.json
        recipe.update(data)
        return jsonify(recipe)
    else:
        return jsonify({"message": "Recipe not found"}), 

# Delete a recipe
@app.route('/recipes/<int:id>', methods=['DELETE'])
def delete_recipe(id):
    global recipes
    recipes = [recipe for recipe in recipes if recipe['id'] != id]
    return jsonify({"message": "Recipe deleted"}), 

# CRUD operations for ingredients

# Read all ingredients
@app.route('/ingredients', methods=['GET'])
def get_ingredients():
    return jsonify(ingredients)

# Create a new ingredient
@app.route('/ingredients', methods=['POST'])
def create_ingredient():
    data = request.json
    new_ingredient = {
        "id": len(ingredients) + 1,
        "name": data['name']
    }
    ingredients.append(new_ingredient)
    return jsonify(new_ingredient), 

# Update an ingredient
@app.route('/ingredients/<int:id>', methods=['PUT'])
def update_ingredient(id):
    ingredient = next((ingredient for ingredient in ingredients if ingredient['id'] == id), None)
    if ingredient:
        data = request.json
        ingredient.update(data)
        return jsonify(ingredient)
    else:
        return jsonify({"message": "Ingredient not found"}), 

# Delete an ingredient
@app.route('/ingredients/<int:id>', methods=['DELETE'])
def delete_ingredient(id):
    global ingredients
    ingredients = [ingredient for ingredient in ingredients if ingredient['id'] != id]
    return jsonify({"message": "Ingredient deleted"}), 
if __name__ == '__main__':
    app.run(debug=True)