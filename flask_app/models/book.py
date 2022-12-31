from flask_app.config.mysqlconnection import connectToMySQL

class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.number_of_pages = data['number_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all_books(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL('books_db').query_db(query)
        books = []
        for book in results:
            books.append(cls(book))
        return books
    
    @classmethod
    def save_book(cls, data):
        query = "INSERT INTO books (title, number_of_pages) VALUES (%(title)s, %(number_of_pages)s);"
        connectToMySQL('books_db').query_db(query, data)
