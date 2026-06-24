from Scripts import activate_this


class Product():
    def __init__(self, name, price, quantity, active=True):
        if name == '':
            raise ValueError("Sorry, name is not allowed to be empty")
        self.name = name

        if 0 > quantity or 0 > price:
            raise Exception("Sorry, no numbers below zero")
        self.price = price
        self.quantity = quantity

        self.active = active

    def get_quantity(self) -> int:
        '''
        Getter function for quantity.
        :return: quantity (int)
        '''
        return self.quantity

    def set_quantity(self, quantity):
        '''
        Setter function for quantity. If quantity reaches 0, deactivates the product.
        :param quantity:
        :return: True if the product is active, otherwise False.
        '''
        if quantity <= 0:
            self.active = False
        self.quantity = quantity

    def is_active(self) -> bool:
        '''
        Getter function for active.
        :return:
        '''
        return self.active


    def activate(self):
        '''
        Activates the product.
        '''
        self.active = True


    def deactivate(self):
        '''
        Deactivates the product
        :return:
        '''
        self.active = False


    def show(self):
        '''
        Prints a string that represents the product, for example:
        "MacBook Air M2, Price: 1450, Quantity: 100"
        :return:
        '''
        print(f'{self.name}, Price: {self.price }, Quantity: {self.quantity}')


    def buy(self, quantity) -> float:
        '''
        Buys a given quantity of the product.
        Updates the quantity of the product.
        In case of a problem, raises an Exception.
        :param quantity:
        :return: total price (float) of the purchase
        '''
        if self.quantity - quantity < 0:
            raise ValueError(f'Sorry, we only have {self.quantity} in stock.')
        else:
            self.set_quantity(self.quantity - quantity)
            return float(quantity * self.price)






bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)

print(bose.buy(50))
print(mac.buy(100))
print(mac.is_active())

bose.show()
mac.show()

bose.set_quantity(1000)
bose.show()