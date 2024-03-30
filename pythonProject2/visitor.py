class Visitor:
    def __init__(self, name, age, nationality, ticket_type, ticket_price):
        self.name = name
        self.age = age
        self.nationality = nationality
        self.ticket_type = ticket_type
        self.ticket_price = ticket_price

    def __str__(self):
        return f"Visitor: {self.name}, Age: {self.age}, Nationality: {self.nationality}, Ticket Type: {self.ticket_type}, Ticket Price: {self.ticket_price}"
