from application import db
from application.models import BlogPost, Users, Books

db.drop_all()
db.create_all()