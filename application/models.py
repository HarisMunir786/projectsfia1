from application import db
from application import login_manager
from flask_login import UserMixin
from datetime import datetime

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    content = db.Column(db.Text, nullable=False, unique=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    def __repr__(self):
        return ''.join([
			'User ID: ', str(self.id), '\r\n',
			'Title: ', self.title, '\r\n', self.content
		])

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)
    posts = db.relationship('Posts', backref='author', lazy=True)
    books= db.relationship('Books', backref='book_ref', lazy=True)
    def __repr__(self):
        return ''.join([
            'User ID: ', str(self.id), '\r\n',
            'Email: ', self.email, '\r\n',
            ])

class Books(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    book_title = db.Column(db.String(30), nullable=False)
    book_author = db.Column(db.String(30), nullable=False)
    book_genre = db.Column(db.String(150), nullable=False, unique=True)
    posts = db.relationship('Posts', backref='author', lazy=True)
    books= db.relationship('Books', backref='book_ref', lazy=True)
    def __repr__(self):
        return ''.join([
            'User ID: ', str(self.id), '\r\n',
            'Email: ', self.email, '\r\n',
            ])