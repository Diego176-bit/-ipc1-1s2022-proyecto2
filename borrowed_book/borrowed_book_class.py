from uuid import uuid4

class BorrowedBook():
    
    def __init__(self,cui,isbn) -> None:
        self.__cui = cui
        self.__isbn = isbn
        self.__uuid = uuid4()
        
    def getCui(self):
        return self.__cui
    
    def getIsbn(self):
        return self.__isbn
    
    def getUuid(self):
        return self.__uuid
    