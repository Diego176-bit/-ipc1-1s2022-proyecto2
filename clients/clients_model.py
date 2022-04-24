class Client:
    def __init__(self, cui, last_name, first_name) -> None:
        self.__cui = cui
        self.__last_name = last_name
        self.__first_name = first_name
        self.__lend = []
    
    def getCui(self):
        return self.__cui
    
    def getLast_name(self):
        return self.__last_name
    
    def getFirst_name(self):
        return self.__first_name
    
    def setLend(self, lend):
        self.__lend.append(lend)
    
    def getData(self):
        return {
            'cui':self.__cui,
            'last_name': self.__last_name,
            'first_name': self.__first_name,
            'record': self.__lend
        }