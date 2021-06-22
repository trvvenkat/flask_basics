from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost/sample"
#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://username:passwd@localhost/databasename"
db = SQLAlchemy(app)


#creating DB table
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #user_id = db.Column(db.Integer, unique=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(150), nullable=False)



from myapp import routes  #example for having all the views in a separate py file
from myapp import views   #example for having all the views in a separate folder