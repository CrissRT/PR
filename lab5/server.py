from flask import Flask, request, jsonify

app = Flask(__name__)

categories = []
products = {}

@app.route('/categories', methods=['GET', 'POST'])
def handle_categories():
    if request.method == 'GET':
        return jsonify(categories)
    elif request.method == 'POST':
        cat = request.json
        cat['id'] = len(categories) + 1
        categories.append(cat)
        products[cat['id']] = []
        return jsonify(cat), 201

@app.route('/categories/<int:cat_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_category(cat_id):
    category = next((c for c in categories if c['id'] == cat_id), None)
    if not category:
        return jsonify({'error': 'Not found'}), 404

    if request.method == 'GET':
        return jsonify(category)
    elif request.method == 'PUT':
        category.update(request.json)
        return jsonify(category)
    elif request.method == 'DELETE':
        categories.remove(category)
        products.pop(cat_id, None)
        return '', 204

@app.route('/categories/<int:cat_id>/products', methods=['GET', 'POST'])
def handle_products(cat_id):
    if cat_id not in products:
        return jsonify({'error': 'Not found'}), 404

    if request.method == 'GET':
        return jsonify(products[cat_id])
    elif request.method == 'POST':
        prod = request.json
        prod['id'] = len(products[cat_id]) + 1
        products[cat_id].append(prod)
        return jsonify(prod), 201

if __name__ == "__main__":
    app.run(debug=True)
