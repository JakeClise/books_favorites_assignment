from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.author import Author




@app.route('/')
def authors():
    authors = Author.get_all_authors()
    return render_template('authors.html', authors = authors)

@app.route('/create-author', methods = ["POST"])
def create_author():
    data = {
        "name": request.form['name']
    }
    Author.save_author(data)
    return redirect('/')