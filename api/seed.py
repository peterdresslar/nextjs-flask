from api.index import app, db, Migration
from datetime import datetime

def seed_migration():
    with app.app_context():
        new_migration = Migration(timestamp=datetime.utcnow())
        db.session.add(new_migration)
        db.session.commit()
        print(f"Added new migration with ID: {new_migration.id}")

if __name__ == "__main__":
    seed_migration()
