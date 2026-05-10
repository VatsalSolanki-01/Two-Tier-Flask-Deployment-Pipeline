from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="mysql-container",
        user="root",
        password="rootvatsal",
        database="quotesdb"
    )

@app.route("/")
def home():
    return jsonify({
        "message": "Two tier Flask MySQL app running",
        "status": "success"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

@app.route("/advice")
def advice():

    db = get_db_connection()

    cursor = db.cursor()

    query = """
    SELECT message FROM quotes
    WHERE category='advice'
    ORDER BY RAND()
    LIMIT 1
    """

    cursor.execute(query)

    result = cursor.fetchone()

    cursor.close()
    db.close()

    return jsonify({
        "category": "advice",
        "message": result[0]
    })

@app.route("/quote")
def quote():

    db = get_db_connection()

    cursor = db.cursor()

    query = """
    SELECT message FROM quotes
    WHERE category='quote'
    ORDER BY RAND()
    LIMIT 1
    """

    cursor.execute(query)

    result = cursor.fetchone()

    cursor.close()
    db.close()

    return jsonify({
        "category": "quote",
        "message": result[0]
    })

@app.route("/joke")
def joke():

    db = get_db_connection()

    cursor = db.cursor()

    query = """
    SELECT message FROM quotes
    WHERE category='joke'
    ORDER BY RAND()
    LIMIT 1
    """

    cursor.execute(query)

    result = cursor.fetchone()

    cursor.close()
    db.close()

    return jsonify({
        "category": "joke",
        "message": result[0]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)