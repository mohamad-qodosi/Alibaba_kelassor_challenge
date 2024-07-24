class Flight:
    def __init__(self, do:str , date:int) -> None:
        self.do = do 
        self.date = date    
    def valid(self) -> None:
        if self.do == "AB" and self.date % 4 == 1 :
            return self  
        elif self.do == "BC" and self.date % 4 == 2 :
            return self  
        elif self.do == "CD" and self.date % 4 == 3 :
            return self  
        elif self.do == "DA" and self.date % 4  == 0 :
            return self 
        else :
            return None 
    

         
    