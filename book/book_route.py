

from flask import Blueprint, request, jsonify
from bookstore_class.Bookstore import db_bookstrore
from book.book_class import Book

book = Blueprint('book', __name__, url_prefix= '/book')

#Agregar un nuevo libro.
@book.route('', methods = ['POST'])
def addBook():
    body = request.get_json()
    try:
        if "isbn" in body and "title" in body and "author" in body and 'year' in body and 'no_copies' in body and 'no_available_copies' in body:
            
                book = Book(body["isbn"], body["title"], body["author"], body['year'], body['no_copies'], body['no_available_copies'])
            
                if db_bookstrore.addBook(book) == True:
                    return {'msg': 'Libro creado exitosamente'}, 201

                elif db_bookstrore.addBook(book) == False:
                    return {'msg' : 'Libro duplicado'}, 400
        else:
            return {'msg' : 'Faltan campos en la peticion'}, 400
    except:
        return {'msg': 'Ocurrio un error en el servidor'}, 500
    
#Modificar un libro.
@book.route('', methods = ['PUT'])
def modifyBook():
    body = request.get_json()
    try:
        if 'isbn' in body and 'title' in body and 'author' in body:
            bookmodify = Book(body["isbn"], body["title"], body["author"])
            if db_bookstrore.modifyBook(bookmodify):
                return {'msg': 'Libro modificado con exito'}, 201
            return {'msg': 'Libro no encontrado'},400
    except:
        return {'msg': 'error en el servidor'}, 500


#Buscar un libro.
@book.route('')
def serchBook():
    title = request.args.get('title')
    author = request.args.get('author')
    year_from = request.args.get('year_from')
    year_to = request.args.get('year_to')
    try:
        libraryBooks = db_bookstrore.getBooks()
        if title != None:
            libraryBooks = db_bookstrore.getBooktitle(libraryBooks, title)
        
        if author !=None:
            libraryBooks = db_bookstrore.getBookAuthor(libraryBooks, author)
    
        libraryBooks = db_bookstrore.getBookFromYear(libraryBooks, year_from, year_to)
    
        return jsonify(libraryBooks),201
    except:
        return {'msg': 'error en el servidor'},500
    
    