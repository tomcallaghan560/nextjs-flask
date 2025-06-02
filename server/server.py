from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/home")
def home():
    return jsonify({"message": "Hello from Flask!", "people": ["Tom", "Sarah", "Jake"]})

@app.route("/api/upload", methods=["POST"])
def upload_pdf():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if not file.filename.endswith(".pdf"):
        return jsonify({"error": "Only PDF files allowed"}), 400

    # You can save it to disk or process it here
    file.save(f"./uploads/{file.filename}")
    return jsonify({"message": f"Received file: {file.filename}"}), 200

if __name__ == "__main__":
    app.run(debug=True, port=8080)