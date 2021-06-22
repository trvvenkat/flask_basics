from myapp import app, Users, db
from flask import request, render_template, redirect, Blueprint




usercontrol = Blueprint("usercontrol", __name__)




@app.route("/signup", methods=['GET','POST'])
def signup():
    #logic
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