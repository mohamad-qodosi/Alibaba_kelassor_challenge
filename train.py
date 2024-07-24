class Train:
    def __init__(self, do:str, date:int):
        self.do  = do 
        self.date = date
    def valid(self):
        if self.do in ["AB","BA","BC","CB","DC","CD"]:
            return self 
        else :
            return None