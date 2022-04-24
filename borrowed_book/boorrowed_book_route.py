
from flask import Blueprint, request
from borrowed_book.borrowed_book_class import BorrowedBook
from bookstore_class.Bookstore import db_bookstrore

borrowed = Blueprint('borrowed', __name__, url_prefix ='/borrow')

@borrowed.route('', methods = ['POST'])
def borrow():
    body = request.get_json()
    
    if 'cui' in body and 'isbn' in body:
        
        borrow = BorrowedBook(body['cui'], body['isbn'])
        if db_bookstrore.addBorrow(borrow):
            return {'msg': 'Prestamo exitoso',
                    'uuid': borrow.getUuid()},200
        return {'msg': 'Faltan campos o no se encontraron los datos solicitados.'},400

@borrowed.route('', methods = ['PATCH'])
def returnBorrow():
    uuid = request.args.get('uuid')
    if db_bookstrore.returnBorrow(uuid):
        return {'msg': 'Libro devuelto exitosamente'}
    return{'msg': 'No hay registro del libro prestado.'}