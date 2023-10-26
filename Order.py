class Order:
    def __init__(self, customer, items) -> None:
        self.customer = customer 
        total = 0
        for item in items:
            total += item.price
        self.bill = total   