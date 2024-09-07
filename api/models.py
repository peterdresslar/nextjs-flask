from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Migration(db.Model):
    __tablename__ = "migrations"

    id = db.Column(db.Integer, primary_key=True, index=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)