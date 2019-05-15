# app.js

# Import necessary libraries. 
from flask import Flask, make_response, redirect, request, jsonify, url_for, request, redirect, url_for, send_from_directory, render_template
import random, string
# from lib import database

#region Data-base stuff

#endregion

#region Server stuff

# Setup Flask app.
app = Flask(__name__)
app.debug = True


# /api, post\get methods
@app.route('/api/login_post_db', methods = ['POST'])
def post_javascript_data():
    jsdata = request.form['canvas_data']
    d = {"d" : 'retrived data is : ' + jsdata }
    return jsonify(d)


# Routes

# root\default route
@app.route('/')
def root():
  return render_template('index.html')

# Login route
@app.route('/login')
def login_route():
    return ''


# profile\user page 
@app.route('/user/<username>')
def userpage(username):
  return render_template('user.html', user = username)

# Run server.
if __name__ == '__main__':
  app.run()

#endregion End of server stuff
  