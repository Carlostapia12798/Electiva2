from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

# Configurar la conexión a MySQL
db_config = {
    "host": os.getenv("DB_HOST", "mysql"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "root"),
    "database": os.getenv("DB_NAME", "testdb")
}

@app.route("/")
def hello():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT '¡Hola, Mundo desde MySQL!'")
        result = cursor.fetchone()
        return f"{result[0]}"
    except Exception as e:
        return f"Error conectando a MySQL: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
