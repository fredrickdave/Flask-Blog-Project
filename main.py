from app import app, db
from app.models import Post, User
from app import email

@app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User, "Post": Post}
