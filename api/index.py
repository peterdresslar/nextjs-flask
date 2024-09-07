from flask import Flask, jsonify
from .models import db, migrate, Migration
from .commands import init_app as init_commands
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("POSTGRES_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app, db)
init_commands(app)

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