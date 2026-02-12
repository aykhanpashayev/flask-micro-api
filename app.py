from flask import Flask, jsonify, request

# Create Flask app
app = Flask(__name__)

# Sample in-memory data
DATA = [
    {"id": 1, "name": "Item One"},
    {"id": 2, "name": "Item Two"}
]

# Used to generate new IDs
next_id = 3


# -------------------------
# GET /hello
# Returns a welcome message
# -------------------------
@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Welcome to my Flask Micro API!"}), 200


# -------------------------
# GET /data
# Returns all stored data
# -------------------------
@app.route("/data", methods=["GET"])
def get_data():
    return jsonify(DATA), 200


# -------------------------
# POST /data
# Adds a new item
# -------------------------
@app.route("/data", methods=["POST"])
def add_data():
    global next_id

    # Get JSON from request body
    new_item = request.get_json()

    # Basic validation
    if not new_item or "name" not in new_item:
        return jsonify({"error": "Invalid input"}), 400

    # Create new item
    item = {
        "id": next_id,
        "name": new_item["name"]
    }

    DATA.append(item)
    next_id += 1

    return jsonify(item), 201


# Run the app
if __name__ == "__main__":
    app.run(debug=True, port=5050)
