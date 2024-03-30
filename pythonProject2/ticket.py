class Ticket:
    def __init__(self, type, price, vat):
        self.type = type
        self.price = price
        self.vat = vat

    def __str__(self):
        return f"Ticket Type: {self.type}, Price: {self.price}, VAT: {self.vat}"
