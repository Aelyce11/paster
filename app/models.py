from app import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), index=True)
    content = db.Column(db.String(1024))
    path = db.Column(db.String(4), index=True, unique=True)
