from flask import Flask, jsonify

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return jsonify({
        "message": "Flask app is running ",
        "status": "success"
    })

# Health check route (important for DevOps)
@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    }), 200

# Additional test route
@app.route("/hello")
def hello():
    return "Hello from Flask CI/CD project!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)