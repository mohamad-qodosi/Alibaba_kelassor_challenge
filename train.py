class train:
    def __init__(self,do,date):
        self.do  = do 
        self.date = date
    def valid(self):
        if self.do == "AB" or self.do == "BA" or self.do == "BC" or self.do == "CB" or self.do == "DC" or self.do == "CD" :
            return True
        else :
            return False