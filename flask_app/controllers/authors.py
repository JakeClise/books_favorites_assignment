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

@app.route('/one_author')
def go_to_author():
    return render_template('one_author.html',user="Bill", book = "How to Be a Baw", number = 900)

@app.route('/add_author_favotite', methods = ["POST"])
def add_author_favorite():
    data = {
        "author_id": request.form['author_id'], 
        "book_id": request.form['book_id']
    }
    Author.save_author_favorite(data)
    return redirect('/one-author')