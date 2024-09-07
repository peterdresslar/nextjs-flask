from flask.cli import with_appcontext
import click
from .models import db, Migration

@click.command('record-migration')
@with_appcontext
def record_migration_command():
    """Record a new migration in the custom migrations table."""
    new_migration = Migration()
    db.session.add(new_migration)
    db.session.commit()
    click.echo(f'Recorded new migration with ID: {new_migration.id}')

def init_app(app):
    app.cli.add_command(record_migration_command)
