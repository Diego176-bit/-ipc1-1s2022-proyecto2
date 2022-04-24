
from book.book_class import Book


class Bookstore:
    
    def __init__(self) -> None:
        
        #Libro
        self.__book = []
        self.__isbn = []
        self.__title = []
        self.__author = []
        self.__year = []
        self.__no_copies = []
        self.__no_avalible_copies = []
        
        #clientes
        self.__clients = []
        self.__cui = []
        self.__name = []
        self.__lastname = []
        
        #prestamos
        self.__borrow = []
        self.__cui_lend = []
        self.__uuid = []
        
        
        
    """Libros"""
    #Se agrega un nuevo libro.    
    def addBook(self, book) -> bool:
        if not book.getIsbn() in self.__isbn:
            self.__book.append(book)
            self.__isbn.append(book.getIsbn())
            self.__title.append(book.getTitle())
            self.__author.append(book.getAuthor())
            self.__year.append(book.getYear())
            self.__no_copies.append(book.getNocopies())
            self.__no_avalible_copies.append(book.getNoavailableCopies())
            
            return True
        else:
            return False
        


    #Modificacion de un libro.
    def modifyBook(self, book) -> bool:
        if book.getIsbn() in self.__isbn:
            for x in self.__isbn:
                if x == book.getIsbn():
                    position = self.__isbn.index(book.getIsbn())
                    self.__isbn[position] = book.getIsbn()
                    self.__title[position] = book.getTitle()
                    self.__author[position] = book.getAuthor()
                    return True

    #Consulta de libro por titulo
    def getBooktitle(self,library,title):
        
        return [book for book in library if book['title'].lower() == title.lower()]
    
    #Consulta de libro por autor
    def getBookAuthor(self, library, author):
        return [book for book in library if book['author'].lower() == author.lower()]
    
    #Consulta de libro por fecha
    def getBookFromYear(self, library, fromYear, toYear):
        
        if fromYear == None:
            fromYear = 0
        if toYear == None:
            toYear = 3000

        return [book for book in library if book['year'] > int(fromYear) and book['year'] < int(toYear)]
    
    def getBooks(self):
        listBooks = []
        for book in self.__book:
            listBooks.append(book.getBook())
        return listBooks
    
    '''Clientes'''
    
    #Agregar un nuevo cliente
    def addClient(self, client):
        
        if not client.getCui() in self.__cui:
            self.__clients.append(client)
            self.__cui.append(client.getCui())
            self.__name.append(client.getFirst_name())
            self.__lastname.append(client.getLast_name())
            return True
            
        return False
    #Obtener datos del cliente.
    def getClient(self, cui):
        if int(cui) in self.__cui:
            for client in self.__clients:
                if client.getCui()== int(cui):
                    return client
        return None
    
    '''Prestamos'''
    
    def addBorrow(self, borrow):
            if not borrow.getCui() in self.__cui_lend:
                self.__borrow.append(borrow)
                self.__cui_lend.append(borrow.getCui())
                self.__uuid.append(str(borrow.getUuid()))
                for book in self.__book:
                    if book.getIsbn() == borrow.getIsbn():
                        book.setNoavailableCopies(-1)
                        return True
    
    def returnBorrow(self, uuid) ->bool:
        if str(uuid) in self.__uuid:
            for borrow in self.__borrow:
                if borrow.getCui() in self.__cui:
                    if str(borrow.getUuid()) == str(uuid):
                        isbn = borrow.getIsbn()
                        for book in self.__book:
                            if book.getIsbn() == isbn:
                                self.__cui_lend.remove(borrow.getCui())
                                self.__uuid.remove(str(borrow.getUuid()))
                                book.setNoavailableCopies(1)
                                return True
    
db_bookstrore = Bookstore()