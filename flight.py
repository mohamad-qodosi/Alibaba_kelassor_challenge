class flight:
    def __init__(self, do:str , date:int) -> None:
        self.do = do 
        self.date = date    
    def valid(self) -> None:
        if self.do == "AB" and self.date % 4 == 1 :
            return True 
        elif self.do == "BC" and self.date % 4 == 2 :
            return True 
        elif self.do == "CD" and self.date % 4 == 3 :
            return True 
        elif self.do == "DA" and self.date % 4  == 0 :
            return True 
        else :
            return False
    def re_ticket(self):
        if self.valid() :
            return self
    

         
    