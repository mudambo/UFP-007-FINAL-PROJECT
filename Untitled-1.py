class Ticket:
    def __init__(self,name, base_price):
        self.name = name
        self.base_price = base_price

    def price(self):
        return self.base_price


concert = Ticket("Concert", 200) 
museum = Ticket("Museum", 150)
print(concert.name,concert.price())  # Output: 200
print(museum.name,museum.price())   # Output: 150

