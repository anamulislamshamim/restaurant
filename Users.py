from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, name, phone, email, address) -> None:
        self.name = name
        self.phone = phone 
        self.email = email 
        self.address = address 


class Customer(User):
    def __init__(self, name, phone, email, address, money) -> None:
        super().__init__(name, phone, email, address)
        self.wallet = money
        self.__order = None
        self.due = 0
    
    @property
    def order(self):
        return self.__order 
    
    @order.setter
    def order(self, order):
        self.__order = order
    
    def place_order(self, order):
        self.order = order 
        self.due = order.bill
        print(f"{self.name} placed an order for {order.items}\nBill: {self.due}")
    
    def pay_for_order(self, amount):
        if self.wallet >= amount:
            self.wallet -= amount 
    
    def give_tips(self, amount):
        pass 

    def write_review(self, starts):
        pass 


class Employee(User):
    def __init__(self, name, phone, email, address, salary, starting_date, department) -> None:
        super().__init__(name, phone, email, address)
        self.salary = salary
        self.starting_department = starting_date
        self.department = department 


class Chef(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, department, cooking_items) -> None:
        super().__init__(name, phone, email, address, salary, starting_date, department)
        self.cooking_items = cooking_items
        self.due = salary 
    
    def receive_salary(self):
        self.due = 0

class Server(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, department) -> None:
        super().__init__(name, phone, email, address, salary, starting_date, department)
    
    def take_order(self, order):
        pass 

    def transfer_order(self, order):
        pass 

    def server_order(self, order):
        pass 

    def receive_tips(self, amount):
        pass 


class Manager(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, department) -> None:
        super().__init__(name, phone, email, address, salary, starting_date, department)


