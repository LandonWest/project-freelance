from app import app, db
from app.models.user import User, UserSchema
from app.models.address import Address


@app.shell_context_processor
def make_shell_context():
    """Convenience method that imports resources when using `flask shell`"""
    return {"db": db, "User": User, "Address": Address, "UserSchema": UserSchema}
