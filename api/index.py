from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("POSTGRES_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Migration(db.Model):
    __tablename__ = "migrations"
    id = db.Column(db.Integer, primary_key=True, index=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

@app.route("/api/python")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/api/migration")
def get_latest_migration():
    latest_migration = Migration.query.order_by(Migration.id.desc()).first()
    
    if latest_migration:
        seconds_ago = int((datetime.utcnow() - latest_migration.timestamp).total_seconds())
        return jsonify({
            "id": latest_migration.id,
            "seconds_ago": seconds_ago
        })
    else:
        return jsonify({"error": "No migrations found"}), 404

@app.route("/api/migrate", methods=["POST"])
def create_migration():
    new_migration = Migration()
    db.session.add(new_migration)
    db.session.commit()
    return jsonify({"id": new_migration.id, "timestamp": str(new_migration.timestamp)})