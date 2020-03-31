from models import User, db
from app import app


db.drop_all()
db.create_all()

User.query.delete


user1 = User(username="ulrika", password="secret", 
             email="ulrika@user.com", first_name="Ulrika",
             last_name="Smith")

user2 = User(username="genna", password="secret2", 
             email="genna@user.com", first_name="Genna",
             last_name="Mergola")
db.session.add(user1)
db.session.add(user2)
db.session.commit()
