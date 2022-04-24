from flask import Blueprint, request
from clients.clients_model import Client
from bookstore_class.Bookstore import db_bookstrore

client = Blueprint('client', __name__, url_prefix='/person')

@client.route('', methods = ['POST'])
def addClient():
    
    body = request.get_json()
    
    if 'cui' in body and 'last_name' in body and 'first_name' in body:
        
        client = Client(body['cui'], body['last_name'], body['first_name'])
        
        if db_bookstrore.addClient(client):
            return {'msg': 'Cliente creado exitosamente'}, 201
        
        return {'msg': 'Cliente ya existente'}, 400
        
@client.route('<cui>')
def getClient(cui):
    try:
        client = db_bookstrore.getClient(cui)
        if client != None:
            return client.getData(),200
        else:
            return {'msg': 'no se encontro el cliente'}
    except:
        return {'msg': 'Error en el servidor'},500