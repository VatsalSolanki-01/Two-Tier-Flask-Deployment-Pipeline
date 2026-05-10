from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL connection function
def get_db_connection():
    connection = mysql.connector.connect(
        host="mysql-container",
        user="root",
        password="rootvatsal",
        database="quotesdb"
    )
    return connection

# Home route
@app.route("/")
def home():
    try:
        db = get_db_connection()

        return jsonify({
            "message": "Flask app is running",
            "database": "MySQL Connected Successfully",
            "status": "success"
        })

    except Exception as e:
        return jsonify({
            "message": "Database connection failed",
            "error": str(e),
            "status": "failed"
        }), 500

# Health check route
@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    }), 200

# Additional test route
@app.route("/hello")
def hello():
    return "Hello from Flask CI/CD two tier project!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)