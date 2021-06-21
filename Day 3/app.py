from flask import Flask, render_template, request, redirect
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





@app.route('/')
def sample():
     return render_template("signup.html")






@app.route("/login/<id>")
def login_hey(id):

    #all_users = Users.query.all()    ----  to get all the values from the DB

    users = Users.query.filter_by(email='manjunath@test.com').all() #  --- to get users by specific condition
    us = Users.query.filter_by(id=id).first() #  --- to select a particular user by specific condition


    #to print all the names of the users we got
    for user in users:
        print(user.name)

    #print(users)


    return render_template("login.html", username=us.name)








@app.route("/allusers")
def all_users():

    allusers = Users.query.all() # --- get all the values from the DB
    return render_template("all_users.html", users=allusers)







@app.route("/signup", methods=['GET','POST'])
def signup():
    if request.method=='GET':
        return render_template("signup.html")
    

    data = request.form
    rname = data['name']
    remail = data['email']


    new_user = Users(name=rname, email=remail)
    db.session.add(new_user)
    db.session.commit()


    # print (rname)
    # print(remail)
    return render_template("login.html", username=rname)

 





if __name__ == '__main__':
    app.run(debug=True)

