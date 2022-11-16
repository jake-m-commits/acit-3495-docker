from app import app
from flask import render_template, redirect, request


@app.route("/", methods=[ "GET", "POST" ])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'node' and request.form['password'] == 'node':
            return redirect('http://localhost:3000/home')
        elif request.form['username'] == 'flask' and request.form['password'] == 'flask':
            return redirect('http://localhost:5001/home')
        else:
            error = 'Invalid Credentials. Please try again.'
    return render_template('public/login.html', error=error)
