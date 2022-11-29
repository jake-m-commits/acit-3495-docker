from app import app
from flask import render_template, redirect, request
import os

# node = os.getenv('NODE_LOAD_BALANCER_SERVICE_HOST')
# flask = os.getenv('RESULT_LOAD_BALANCER_SERVICE_HOST')

@app.route("/", methods=[ "GET", "POST" ])
def login():
    error = None
    if request.method == 'POST':
        host = request.host.split(':')[0]
        if request.form['username'] == 'node' and request.form['password'] == 'node':            
            return redirect(f'http://{host}:3000/home')
        elif request.form['username'] == 'flask' and request.form['password'] == 'flask':
            return redirect(f'http://{host}:5001/home')
        else:
            error = 'Invalid Credentials. Please try again.'
    return render_template('public/login.html', error=error)
