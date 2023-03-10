from flask_app.config.mysqlconnection import connectToMySQL

class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorite_books = []
        self.unfavorited_books = []        

    @classmethod
    def get_all_authors(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL('books_db').query_db(query)
        authors = []
        for author in results:
            authors.append(cls(author))
        return authors
    
    @classmethod
    def save_author(cls,data):
        query = "INSERT INTO authors (name) VALUES (%(name)s);"
        return connectToMySQL('books_db').query_db(query, data)
    
    @classmethod
    def save_author_favorite(cls, data):
        query = "INSERT INTO favorites (author_id, book_id) VALUES (%(author_id)s, %(book_id)s);"
        return connectToMySQL('books_db').query_db(query, data)
        