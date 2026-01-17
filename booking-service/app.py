from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/bookings")
def bookings():
    return jsonify([
        {"booking_id": 101, "place": "Goa"},
        {"booking_id": 102, "place": "Manali"}
    ])

app.run(host="0.0.0.0", port=5001)

