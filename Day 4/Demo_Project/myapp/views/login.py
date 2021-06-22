from myapp import app, Users
from flask import render_template

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