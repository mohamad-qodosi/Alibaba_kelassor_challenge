from os import system
clear = lambda : system("cls")
def reserve(vehcile):
        date = input("please enter your date")
        org = input("please enter your origin city").upper()
        des = input("please enter your destination").upper()
        
        route = org + des
        
        if vehicle == "plain":
            if type(Flight(route,date).valid()) == Flight:
            	print("succes")
              
            else:
            	reserve(vehicle)
        elif vehicle == "train":
            if type(Train(route,date).valid()) == Train:
            	print("succes")
            else:
            	reserve(vehicle)
        else:
            print("invalid")



def menu():

    print("""
        1) train
        2) flight
        3) logout
        4) my ticket
        5) exit
        """)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        reserve(train)
    elif choice == 2:
        reserve(flight)
    elif choice == 3:
        logout()
    elif choice == 4:
        pass
    elif choice == 5:
        exit()
















