class Restaurant:
    def __init__(self, name, rent, menu) -> None:
        self.name = name 
        self.orders = []
        self.rent = rent 
        self.chef = []
        self.server = []
        self.manager = [] 
        self.menu = menu
        self.revenue = 0
        self.expense = 0
        self.profit = 0
        self.balance = 0

    def add_employee(self, employee_type, employee):
        etype = employee_type.lower()
        if etype == 'chef':
            self.chef.append(employee)
        elif etype == 'server':
            self.server.append(employee)
        elif etype == 'manager':
            self.manager.append(employee)
    
    def add_menu(self, item):
        self.menu.append(item)
    
    def receive_payment(self, order, amount, customer):
        if order not in self.orders:
            self.orders.append(order)

        if amount >= order.bill:
            self.revenue += order.bill 
            self.balance += order.bill 
            customer.due = 0
            return amount - order.bill  
    
    def pay_rent(self):
        if self.balance >= self.rent:
            self.balance -= self.rent
            print(f"Ater paid {self.rent} taka rent your current balance is {self.balance} taka")
        else:
            print(f"Current balance is not sufficient for {self.rent} rent! Your balance is {self.balance} taka")
    
    def pay_expense(self, amount, expense_type):
        if amount <= self.balance:
            self.balance -= amount
            self.expense += amount 
            print(f"Expense {amount} for {expense_type}")
        else:
            print("You have not sufficient balance!")
    
    def pay_salary(self, employee):
        if employee.salary <= self.balance:
            self.balance -= employee.salary
            employee.receive_salary()
        
    def show_employes(self):
        if self.manager:
            print("Managers:")
            for manager in self.manager:
                print(f"   Name: {manager.name} Dept: {manager.department}")
            print()
        
        if self.chef:
            print("Chefs:")
            for chef in self.chef:
                print(f"   Name: {chef.name} Dept: {chef.department}")
            print()
        
        if self.server:
            print("Servers:")
            for server in self.server:
                print(f"   Name: {server.name} Dept: {server.department}")
            print()

        
    
    