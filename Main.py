from Menu import Pizza, Burger, Drinks, Menu
from Restaurant import Restaurant
from Users import Manager, Chef, Server, Customer
from Order import Order


def main():
    menu = Menu()

    pizza_1 = Pizza('Shutki Pizza', 600, 'large', ['shutki', 'onion'])
    menu.add_menu_item('pizza', pizza_1)

    pizza_2 = Pizza('Alur Vorta Pizza', 400, 'large', ['Potato', 'oil', 'onion'])
    menu.add_menu_item('pizza', pizza_2)

    pizza_3 = Pizza('Dal Pizza', 500, 'large', ['Dal', 'oil', 'onion'])
    menu.add_menu_item('pizza', pizza_3)

    burger_1 = Burger('Naga Burger', 1000, 'chicken', ['bread', 'chili'])
    menu.add_menu_item('burger', burger_1)

    drinks_1 = Drinks('Speed', 30, True)
    menu.add_menu_item('drinks', drinks_1)

    # show menu
    menu.show_menu()

    # create restaurant 
    restaurant = Restaurant("Shahi Baba", 2000, menu)

    # appoint a manager 
    manager = Manager('Kala Chan', 10502, 'kala@chan.com', 'kalipur', 1500, 'Jan 1, 2023', 'management')
    restaurant.add_employee('manager', manager)

    # appoint chef
    chef = Chef("Rustom Baburchi", 105028, 'rustom@baburchi.com', 'pora bari', 800, 'Feb 1, 2023', 'chef', 'pizza')
    restaurant.add_employee('chef', chef)
    # appoint a waiter
    server = Server('Chotu Babu', 10400, 'choto@babu.com', 'kaligong', 380, 'Feb 1, 2023', 'server')
    restaurant.add_employee('server', server)

    # show employees
    restaurant.show_employes()

    # customers
    customer_1 = Customer("sakib khan", 483948, 'sakib@khan.com', 'banani', 100000)
    order1 = Order(customer_1, [pizza_1, burger_1, drinks_1])
    restaurant.receive_payment(order1, order1.bill, customer_1)

    customer_2 = Customer("sakib khan", 483948, 'sakib@khan.com', 'banani', 100000)
    order2 = Order(customer_2, [pizza_1, burger_1, drinks_1])
    restaurant.receive_payment(order2, order2.bill, customer_2)

    print(restaurant.revenue, restaurant.balance)
    print(restaurant.orders)
    restaurant.pay_rent()
if __name__ == "__main__":
    main()