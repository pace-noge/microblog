from app import app, db
from app.models import User, Post
from app import cli


@app.shell_context_processor
def make_shell():
    return {'db': db, 'User': User, 'Post': Post}


