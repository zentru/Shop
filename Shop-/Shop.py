class NotEnoughFunds(Exception):
    pass


class Shop:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.fleet = []

    def payday(self, money):  # Зарплата
        self.balance -= money

    def goods_sell(self, money):  # Продаж товарів
        self.balance = money

    def add_funds(self, amount):
        self.balance += amount

    def rent_shop(self, money):
        self.balance -= money

class Cashier:
    def __init__(self, position, name, salary, experience, age):
        self.experience = experience
        if self.experience >=1:
            self.position = position
            self.salary = salary
            self.age = age
            self.name = name
            self.get_work = True
        else:
            self.get_work = False
    
class Guardian:
    def __init__(self, position, name, salary, experience, age):
        self.experience = experience
        if self.experience >=1:
            self.position = position
            self.salary = salary
            self.age = age
            self.name = name
            self.get_work = True
        else:
            self.get_work = False

class Manager:
    def __init__(self, position, name, salary, experience, age):
        self.experience = experience
        if self.experience >=1:
            self.position = position
            self.salary = salary
            self.age = age
            self.name = name
            self.get_work = True
        else:
            self.get_work = False

class Customers:
    def __init__(self, name, goods, money):
        self.goods = goods
        self.money = money
        if self.money >0:
            self.goods >=1
            self.money = money
            self.goods = goods
            self.name = name
            self.buy_goods = True
        else:
            self.buy_goods = False
       
class Rent:
    def __init__(self, price):
        self.price = price
        if self.price >=1:
            self.rent_s = True
        else:
            self.rent_s = False

def main():
    # Назва магазину
    shopcompany = Shop("АТБ")
    print(shopcompany)
    # Назва магазину
    # Касир
    cashier = Cashier('Cashier', 'Maria', 4500, 2, 24)
    if cashier.get_work == True:
        print(f'Employee:{cashier.position, cashier.name, cashier.age} was accept')
        shopcompany.payday(cashier.salary)
    else:
        print("{cashier.name} don't have enough experience")
    # Касир
    # Охоронець
    guardian = Guardian('Guardian', 'Yevgen', 5800, 3, 27)
    if guardian.get_work == True:
        print(f'Guardian:{guardian.position, guardian.name, guardian.age} was accept')
        shopcompany.payday(guardian.salary)
    else:
        print("{guardian.name} don't have enough experience")
    # Охоронець
    # Менеджер
    manager = Manager('Manager', 'Vika', 6700, 1, 21)
    if manager.get_work == True:
        print(f'Manager:{manager.position, manager.name, manager.age} was accept')
        shopcompany.payday(manager.salary)
    else:
        print("{manager.name} don't have enough experience")
    # Менеджер
    # Покупець
    customers = Customers('Tomato', 10, 500)
    if customers.buy_goods == True:
        print(f'Customers:{customers.name, customers.goods} sell') 
        shopcompany.goods_sell(customers.money)
    else:
        print("Customers don't have enough money")
    # Покупець
    # Оренда
    rent = Rent(100000)
    if rent.rent_s == True:
        print(f'Rent:{rent.price} The rent is paid')
        shopcompany.rent_shop(rent.price)
    else:
        print("Your shop don't have enough money")
    # Оренда
    # Кредит
    shopcompany.add_funds(200000)
    print(f'{shopcompany.balance} all balance')
    # Кредит
main()
