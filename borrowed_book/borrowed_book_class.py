from uuid import uuid4
from datetime import datetime

class BorrowedBook():
    
    def __init__(self,cui,isbn) -> None:
        self.__cui = cui
        self.__isbn = isbn
        self.__uuid = uuid4()
        self.__date = datetime.now()
        
    def getCui(self):
        return self.__cui
    
    def getIsbn(self):
        return self.__isbn
    
    def getUuid(self):
        return self.__uuid
    
    def getBorrow(self):
        return {'isbn': self.__isbn,
                'uuid': self.__uuid,
                'date_borrow': self.__date}