from flask_app import app
from flask_app.controllers import authors


'''
@app.route('/go-add-book')
def go_add_book():
    return render_template('add_book.html')
    '''



if __name__ == "__main__":
    app.run(debug=True)