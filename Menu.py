class Food:
    def __init__(self, name, price) -> None:
        self.name = name 
        self.price = price
        self.cookin_time = 15
    

class Burger(Food):
    def __init__(self, name, price, meat, ingridients) -> None:
        super().__init__(name, price)
        self.meat = meat 
        self.ingridients = ingridients
    

class Pizza(Food):
    def __init__(self, name, price, size, toppings) -> None:
        super().__init__(name, price)
        self.size = size
        self.toppings = toppings


# inheritance relation: is a relation
class Drinks(Food):
    def __init__(self, name, price, isCold=True) -> None:
        super().__init__(name, price)
        self.isCold = isCold 


# composition relation: has a relation
class Menu:
    def __init__(self) -> None:
        self.pizzas = []
        self.burgers = []
        self.drinks = []
    
    def add_menu_item(self, food_type, food):
        ftype = food_type.lower()
        if ftype == 'pizza':
            self.pizzas.append(food)
        elif ftype == 'burger':
            self.burgers.append(food)
        elif ftype == 'drinks':
            self.drinks.append(food)
    
    def remove_menu_item(self, food_type, food):
        ftype = food_type.lower()
        if ftype == 'pizza':
            self.pizzas.remove(food)
        elif ftype == 'burger':
            self.burgers.remove(food)
        elif ftype == 'drinks':
            self.drinks.remove(food)
    
    def show_menu(self):
        if self.pizzas:
            print("Available Pizzas:")
            for pizza in self.pizzas:
                print(f"Name: {pizza.name} Price: {pizza.price}")
            print()
        
        if self.burgers:
            print("Available Burgers:")
            for burger in self.burgers:
                print(f"Name: {burger.name} Price: {burger.price}")
            print()
        
        if self.drinks:
            print("Available Drinks:")
            for drink in self.drinks:
                print(f"Name: {drink.name} Price: {drink.price}")
            print()

