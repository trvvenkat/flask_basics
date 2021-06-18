from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost/sample"
db = SQLAlchemy(app)

#creating a table called USERS in our Sample DB
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(150), nullable=False)





@app.route("/login")
def login_hey():
    msg = "SUCCESS"
    sample = "heyy"
    return render_template("login.html", msg=msg, sample=sample)

@app.route("/signup", methods=['GET','POST'])
def signup():
    if request.method=='GET':
        return render_template("signup.html")
    data = request.form
    name = data['name']
    email = data['email']
    print (name)
    print(email)
    return redirect('/login')

 


if __name__ == '__main__':
    app.run(debug=True)

