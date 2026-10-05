from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Flask backend is running"


@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()

    name = data.get("name", "")
    email = data.get("email", "")
    course = data.get("course", "")

    return jsonify({
        "message": "Form submitted successfully",
        "name": name,
        "email": email,
        "course": course
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
