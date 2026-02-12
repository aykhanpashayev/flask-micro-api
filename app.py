from flask import Flask, jsonify, request

# Create Flask app
app = Flask(__name__)

# Sample in-memory data
DATA = [
    {"id": 1, "name": "Water Bottle"},
    {"id": 2, "name": "Laptop Adapter"}
]

# Used to generate new IDs
next_id = 3

# -------------------------
# Main page
# -------------------------
@app.route("/")
def index():
    return """
    <h1>Flask Micro-API</h1>
    <p>Try these endpoints:</p>
    <ul>
        <li><a href="/hello">/hello</a></li>
        <li><a href="/data">/data</a></li>
        <li><a href="/data/1">/data/1</a></li>
    </ul>
    <p>Use Postman for: <b>POST /data</b></p>
    """

# -------------------------
# GET /hello
# Returns a welcome message
# -------------------------
@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Welcome to my Flask Micro API! That has very important data inside"}), 200


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

    if not request.is_json:
        return jsonify({"error": "Send JSON with Content-Type: application/json"}), 400

    new_item = request.get_json()

    if "name" not in new_item:
        return jsonify({"error": "Missing 'name' field"}), 400

    item = {"id": next_id, "name": new_item["name"]}
    DATA.append(item)
    next_id += 1

    return jsonify(item), 201

# -------------------------
# Items by their IDs
# -------------------------
@app.route("/data/<int:id>")
def item(id):
    for i in DATA:
        if i["id"]==id:
            return jsonify(i), 200

    return jsonify({"error":"Item not found"}), 404

# Run the app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5050)

