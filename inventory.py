from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql.kishore@12",
    database="inventory"
)

cursor = db.cursor()


@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    phone_no = data['phone_no']
    name = data['name']
    email = data['email']
    address = data['address']
    pincode = data['pincode']
    state = data['state']
    age = data['age']
    password = data['password']
    cursor.execute("INSERT INTO Users (user_phone_no, user_name, user_email, user_address, user_pincode, user_state, user_age, user_password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                   (phone_no, name, email, address, pincode, state, age, password))
    db.commit()
    return jsonify({"message": "User registered successfully"}), 201


def fetch_users_from_db():
    cursor.execute("SELECT * FROM Users")
    return cursor.fetchall()


@app.route('/register', methods = ['GET'])
def get_users():
    users_list = []
    users = fetch_users_from_db()
    for user in users:
        users_list.append({
            "user_id": user[0],
            "user_phone_no": user[1],
            "user_name": user[2],
            "user_email": user[3],
            "user_address": user[4],
            "user_pincode": user[5],
            "user_state": user[6],
            "user_age": user[7],
            "user_password": user[8],
        })
        return jsonify(users_list), 200

@app.route('/product', methods=['POST'])
def add_product():
    data = request.get_json()
    name = data['product_name']
    quantity = data['product_qt']
    price = data['product_price']
    shop_details = data['shop_details']
    product_category = data['product_category']
    cursor.execute("INSERT INTO product (product_name, product_qt, product_price, shop_details, product_category) VALUES (%s, %s, %s, %s, %s)",
                   (name, quantity, price, shop_details, product_category))
    db.commit()
    return jsonify({"message": "Product added successfully"}), 201

# Read products
@app.route('/product', methods=['GET'])
def get_products():
    products = fetch_users_from_db()
    product_list = []
    for product in products:
        product_list.append({
            "product_id": product[0],
            "product_name": product[1],
            "product_qt": product[2],
            "product_price": product[3],
            "shop_details": product[4],
            "product_category": product[5]
        })
    return jsonify(product_list), 200

@app.route('/product/<int:product_id>', methods=['GET'])
def get_product(product_id):
    cursor.execute("SELECT * FROM product WHERE product_id = %s", (product_id,))
    product = cursor.fetchone()
    if product:
        return jsonify({
            "product_id": product[0],
            "product_name": product[1],
            "product_qt": product[2],
            "product_price": product[3],
            "shop_details": product[4],
            "product_category": product[5]
        }), 200
    return jsonify({"message": "Product not found"}), 404

# Update 
@app.route('/product/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    name = data['product_name']
    quantity = data['product_qt']
    price = data['product_price']
    shop_details = data['shop_details']
    product_category = data['product_category']
    cursor.execute("UPDATE product SET product_name = %s, product_qt = %s, product_price = %s, shop_details = %s, product_category = %s WHERE product_id = %s",
                   (name, quantity, price, shop_details, product_category, product_id))
    db.commit()
    return jsonify({"message": "Product updated successfully"}), 200

# Delete 
@app.route('/product/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    cursor.execute("DELETE FROM product WHERE product_id = %s", (product_id,))
    db.commit()
    return jsonify({"message": "Product deleted successfully"}), 200

# Place an order
@app.route('/order', methods=['POST'])
def place_order():
    data = request.get_json()
    order_qt = data['order_qt']
    user_id = data['user_id']
    order_payment = data['order_payment']
    shop_details = data['shop_details']
    cursor.execute("INSERT INTO `order` (order_qt, user_id, order_payment, shop_details) VALUES (%s, %s, %s, %s)",
                   (order_qt, user_id, order_payment, shop_details))
    db.commit()
    return jsonify({"message": "Order placed successfully"}), 201


@app.route('/order', methods=['GET'])
def get_orders():
    cursor.execute("SELECT * FROM `order`")
    orders = cursor.fetchall()
    order_list = []
    for order in orders:
        order_list.append({
            "order_id": order[0],
            "order_qt": order[1],
            "user_id": order[2],
            "order_payment": order[3],
            "shop_details": order[4]
        })
    return jsonify(order_list), 200

@app.route('/order/<int:order_id>', methods=['GET'])
def get_order(order_id):
    cursor.execute("SELECT * FROM `order` WHERE order_id = %s", (order_id,))
    order = cursor.fetchone()
    if order:
        return jsonify({
            "order_id": order[0],
            "order_qt": order[1],
            "user_id": order[2],
            "order_payment": order[3],
            "shop_details": order[4]
        }), 200
    return jsonify({"message": "Order not found"}), 404

# Update 
@app.route('/order/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    data = request.get_json()
    order_qt = data['order_qt']
    user_id = data['user_id']
    order_payment = data['order_payment']
    shop_details = data['shop_details']
    cursor.execute("UPDATE orders SET order_qt = %s, user_id = %s, order_payment = %s, shop_details = %s WHERE order_id = %s",
                   (order_qt, user_id, order_payment, shop_details, order_id))
    db.commit()
    return jsonify({"message": "Order updated successfully"}), 200

# Delete 
@app.route('/order/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    cursor.execute("DELETE FROM `order` WHERE order_id = %s", (order_id,))
    db.commit()
    return jsonify({"message": "Order deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
