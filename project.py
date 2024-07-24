class Train:
    def __init__(self,do,date):
        self.do  = do 
        self.date = date
    def valid(self):
        if self.do == "AB" or self.do == "BA" or self.do == "BC" or self.do == "CB" or self.do == "DC" or self.do == "CD" :
            return self 
        else :
            return None
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
    

         
class User:
    def __init__(self, user_name: str , password : int) -> None:
        self.username = user_name
        self.password = password
        self.train_tikets = []
        self.flight_tickets = []
    def add_train_ticket(self, train : Train): # type: ignore
        self.train_tikets.append(train)
    def add_flight_ticket(self, flight : Flight): # type: ignore
        self.flight_tickets.append(flight)
    def get_train_tickets(self):
        return self.train_tikets
    def get_flight_tickets(self):
        return self.flight_tickets
    
print('welcome to alibaba')

users_list=[]

while True:
    inp = ''
    flag = 0
    while True:
        
        inp = input('what do you want to do?  sign in | sign up: ')
        if inp == 'sign in':
            user_name = input('give me your username :')
            password = input('give me your password : ')
            for user in users_list:
                if user.username == user_name and user.password == password :
                    print('successfull login')
                    flag = 1
                    break
            if flag == 1:
                break
            else :
                print('incorrect')

            
        elif inp == 'sign up':
            user_name = input('give me your username :')
            password = input('give me your password : ')
            this_user = User(user_name, password)
            users_list.append(this_user)
        else:
            print('wrong approach')
    while True:
        def reserve(vehcile):
                date = input("please enter your date")
                org = input("please enter your origin city").upper()
                des = input("please enter your destination").upper()
                
                route = org + des
                
                if vehcile == "plain":
                    if type(Flight(route,date).valid()) == Flight:
                        print("succes")
                    
                    else:
                        reserve(vehcile)
                elif vehcile == "train":
                    if type(Train(route,date).valid()) == Train:
                        print("succes")
                    else:
                        reserve(vehcile)
                else:
                    print("invalid")



        

        print("""
            1) train
            2) flight
            3) logout
            4) my ticket
            5) exit
            """)
        choice = int(input("Enter your choice: "))
        if choice == 1:
            reserve("train")
        elif choice == 2:
            reserve("flight")
        elif choice == 3:
            break
        elif choice == 4:
            for user in users_list:
                user : User
                if user.username == user_name:
                    user_train_ticekts = user.get_train_tickets()
                    user_train_flight = user.get_flight_tickets()
                    print(user_train_ticekts)
                    print(user_train_flight)

                    
        elif choice == 5:
            exit()
            
