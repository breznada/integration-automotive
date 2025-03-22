from flask import Flask, request, jsonify

app = Flask(__name__)

VALID_PART_NAMES = [
    "Engine Block",
    "Transmission Assembly",
    "Chassis Frame",
    "Brake Disc"
]

@app.route("/process_order", methods=["POST"])
def process_order():
    data = request.get_json()

    part = data.get("part", {})
    part_name = part.get("part_name", "")

    # Validate part_name
    if part_name not in VALID_PART_NAMES:
        return jsonify({"error": "Bad Part Type"}), 400

    response = {
        "order_id": data.get("order_id"),
        "part": {
            "part_id": part.get("part_id"),
            "part_name": part_name,
            "part_quantity": part.get("part_quantity")
        },
        "destination_warehouse": {
            "destination_warehouse_id": "WH-001",
            "destination_warehouse_place_id": "PL-009",
            "destination_warehouse_name": "Main Warehouse A"
        }
    }

    return jsonify(response), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

