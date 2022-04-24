
class Book:
    def __init__(self, isbn, title, author,year,no_copies, no_available_copies):
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__year = year
        self.__no_copies = no_copies
        self.__no_available_copies = no_available_copies
    
    def getIsbn(self):
        return self.__isbn
    
    def getTitle(self):
        return self.__title
    
    def getAuthor(self):
        return self.__author
    
    def getYear(self):
        return self.__year
    
    def getNocopies(self):
        return self.__no_copies
    
    def getNoavailableCopies(self):
        return self.__no_available_copies
    
    def setNoavailableCopies(self, copies):
        self.__no_available_copies +=copies
    
    def getBook(self):
        return {
            'isbn' : self.__isbn,
            'title' : self.__title,
            'author' : self.__author,
            'year': self.__year,
            'no_avalible_copies': self.__no_available_copies,
            'no_copies': self.__no_copies
        }