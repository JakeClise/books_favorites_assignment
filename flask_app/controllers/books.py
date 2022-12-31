from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.book import Book


@app.route('/go-add-book')
def go_add_book():
    books = Book.get_all_books()
    return render_template('add_book.html', books = books)

@app.route('/create-book', methods = ["POST"])
def create_book():
    data = {
        "title": request.form['title'],
        "number_of_pages": request.form['number_of_pages']
    }
    Book.save_book(data)
    return redirect('/go-add-book')