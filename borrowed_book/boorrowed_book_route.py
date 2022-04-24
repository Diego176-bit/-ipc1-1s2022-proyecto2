
from flask import Blueprint, request
from borrowed_book.borrowed_book_class import BorrowedBook
from bookstore_class.Bookstore import db_bookstrore

borrowed = Blueprint('borrowed', __name__, url_prefix ='/borrow')

@borrowed.route('', methods = ['POST'])
def borrow():
    body = request.get_json()
    try:
        if 'cui' in body and 'isbn' in body:
        
            borrow = BorrowedBook(body['cui'], body['isbn'])
            if db_bookstrore.addBorrow(borrow):
                return {'msg': 'Prestamo exitoso',
                    'uuid': borrow.getUuid()},200
            return {'msg': 'Cliente con prestamo ya activo.'},400
    except:
        return {'msg': 'ocurrio un error en el servidor'},500
    
@borrowed.route('', methods = ['PATCH'])
def returnBorrow():
    try:
        uuid = request.args.get('uuid')
        if db_bookstrore.returnBorrow(uuid):
            return {'msg': 'Libro devuelto exitosamente'},200
        return{'msg': 'No hay registro del libro prestado.'},400
    except:
        return {'msg': 'Error en el servidor'},500