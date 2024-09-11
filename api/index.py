from flask import Flask, jsonify
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(os.getenv('DATABASE_URL'))
    return conn

@app.route("/api/data")
def get_data():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM your_table_name')
    data = cur.fetchone()
    cur.close()
    conn.close()
    return jsonify({"id": data[0], "datestamp": data[1].isoformat()})

@app.route("/api/python")
def hello_world():
    return "<p>Hello, World!</p>"