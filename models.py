from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
def connect_db(app):
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """pet model"""

    __tablename__ = 'pets'

    id = db.Column(db.Integer,primary_key=True,autoincrement = True)

    name = db.Column(db.Text,nullable = False)

    species = db.Column(db.Text,nullable = False)

    photo_url = db.Column(db.Text,nullable = True,default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ3Mcq0MzUcuiMk2LiTxsmEUd-jDoXO3h8KYBhCmQg7G_RMnVBPyTO-XGPoE_wVbhobp3E&usqp=CAU')

    age = db.Column(db.Integer,nullable = True)

    notes = db.Column(db.Text,nullable = True)

    available = db.Column(db.Boolean,default=True)