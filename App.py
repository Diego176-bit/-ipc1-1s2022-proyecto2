from flask import Flask, jsonify


from book.book_route import book
from clients.clients_route import client
from borrowed_book.boorrowed_book_route import borrowed
bookstore = Flask(__name__)


@bookstore.route('/')
def index():
    return {'msg': 'hello world'}

bookstore.register_blueprint(book)
bookstore.register_blueprint(client)
bookstore.register_blueprint(borrowed)

if __name__ == '__main__':
    bookstore.run(debug = True)