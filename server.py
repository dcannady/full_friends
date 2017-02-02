from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector

from Tkinter import *
import re

app = Flask(__name__)
app.secret_key = "ThisIsSecret"
mysql = MySQLConnector(app, 'friendsdb') #DATABASE
    #   passing in app and friendsdb as arguments; arguments are what are passed in parameters are what functions have.
NAME_REGEX = re.complile('^[a-zA-Z]') #name regex - no spaces, no numbers
        #  making a variable name_regex that is passing in the variable.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\+--]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
        # This is running the compile function.

#Display ALL FRIENDS *** IS WORKING! DO NOT TOUCH THIS ***

@app.route('/', methods=['POST', 'GET'])
def index(): #handler function
    friends = [] # init empty friend
    # created the variable freinds setting it to an empty list.
    try:
        query = "SELECT * FROM friends"
        friends = mysql.query_db(query)
    except Exception as e:
        flash("Friends are having issues. Try back later.")
        # If the try block returns an error instead of doing what it is suppose too.
    return render_template('index.html', all_friends=friends)

#DISPLAY SINGLE USER RECORD - *** IS WORKING! DO NOT TOUCH ***

@app.route('/friends/<id>', methods=['POST'])
def update(id):
    valOK = false;
    session['view'] = "alert"

    if len(request.form['fname']) < 1:
        flash("First name cannot be empty!")
    elif not NAME_REGEX.match(request.form['fname']):
        flash("First name can only contain letters!")
    elif len(request.form['lname']) < 1:
        flash("Last name cannot be empty!")
    elif not NAME_REGEX.match(request.form['lname']):
        flash("Last name can only contain letters!")
    elif len(request.form['occ'])< 1:
        flash("Occupation cannot be empty!")
    elif not NAME_REGEX.match(request.form['occ']):
        flash("Occupation can only contain letters!")
    else:
        valOK = True
    #Update the record if fields pass all validation.

if (valOK):
    try:
        query = "UPDATE friends SET first_name = '" + request.form['fname'] +'", last_name='" + request.form['lname'] + "', occupation='" + request.form['occ'] + "'
        session['view'] = "success"
        flash("Successfully changed ID " + id)
        mysql.query_db(query)
    except Exception as e:
        session['view'] = "alert"
        flash("Unable to change your friend!")
        return redirect('/friends/' + id + '/edit')
    else:
        return redirect('/friends/' + id + '/edit')
    return redirect('/')

#   DELETE RECORD - *** IS WORKING! DO NOT TOUCH THIS ***

@app.route('/friends/<id>/delete')
def destroy(id):
    try:
        query = "DELETE FROM friends WHERE ID: :id"
        data = {'id': id}
        mysql.query_db(query,data)
    except Exception as e:
        flash("Unable to delete Friend ID: {0}".format(id))
        print e
    return redirect('/')

 #   CREATE NEW FRIEND
 @app.route('/create')
 def create():
     return render_template('add.html')
#     CREATE NEW FRIEND
@app.route('/friends', methods=['POST'])
def saveFriend():
    fname = request.form['fname']
    lname = request.form['occ']
    occ   = request.form['occ']

    valOK = False;
    session['view'] = "alert"

    if len(fname) < 1
        flash("First name cannot be empty!")
    elif not NAME_REGEX.match(fname):
        flash("First name can only contain letters!")
    elif len(lname) < 1:
        flash("Last name cannot be empty!")
    elif not NAME_REGEX.match(lname):
        flash("Last name can only contain letters!")
    else:
        valoK = True
            #Update the record if fields pass all validation.
    if (valOK):
        try:
            query = "INSERT INTO friends"
            query = query + " (first_name, last_name, occupation, created_at, updated_at)"
            query = query + VALUES('" + fname + "', )
            mysql.query_db(query)
            session['view'] = "success"
            flash("Successfully added new friend")
        except Exception as e:
            session['view'] = "alert"
            flash("Unable to add new friend!")
            return redirect('/create')
    else:
        return redirect('/create')
    return redirect('/')
app.run(debug=True)
