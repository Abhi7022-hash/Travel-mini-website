from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/users")
def users():
    return jsonify([
        {"id": 1, "name": "Abhishek"},
        {"id": 2, "name": "Rahul"}
    ])

app.run(host="0.0.0.0", port=5000)

