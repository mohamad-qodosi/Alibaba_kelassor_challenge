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


    

        
