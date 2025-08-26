from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Sample in-memory data
USERS = [
    {"id": 1, "name": "Ana Silva", "email": "ana@example.com"},
    {"id": 2, "name": "Bruno Costa", "email": "bruno@example.com"},
    {"id": 3, "name": "Carla Souza", "email": "carla@example.com"}
]

PRODUCTS = [
    {"id": 1, "name": "Carro Popular", "price": 25000},
    {"id": 2, "name": "Sedan Confort", "price": 48000},
    {"id": 3, "name": "SUV Turbo", "price": 78000}
]

ORDERS = []
NEXT_ORDER_ID = 1

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"}), 200

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(USERS), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in USERS if u['id'] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(PRODUCTS), 200

@app.route('/orders', methods=['POST'])
def create_order():
    global NEXT_ORDER_ID
    data = request.get_json()
    if not data or 'user_id' not in data or 'product_ids' not in data:
        return jsonify({"error": "Missing fields. Required: user_id, product_ids"}), 400
    user = next((u for u in USERS if u['id'] == data['user_id']), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    items = []
    total = 0
    for pid in data['product_ids']:
        p = next((pr for pr in PRODUCTS if pr['id'] == pid), None)
        if not p:
            return jsonify({"error": f"Product id {pid} not found"}), 404
        items.append(p)
        total += p['price']
    order = {
        "id": NEXT_ORDER_ID,
        "user": user,
        "items": items,
        "total": total
    }
    NEXT_ORDER_ID += 1
    ORDERS.append(order)
    return jsonify(order), 201

@app.route('/orders', methods=['GET'])
def list_orders():
    return jsonify(ORDERS), 200

if __name__ == '__main__':
    # Run in debug mode for development. Use a production server (gunicorn) for production.
    app.run(host='0.0.0.0', port=5000, debug=True)
