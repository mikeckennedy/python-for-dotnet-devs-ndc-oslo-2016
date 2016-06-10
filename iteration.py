class ShoppingChart:
    def __init__(self):
        self.cart_items = []

    def add(self, item):
        self.cart_items.append(item)

    def __iter__(self):
        return self.cart_items.__iter__()

    @property
    def total(self):
        t = 0
        for i in self.cart_items:
            t += i.price
        return t


class CartItem:
    def __init__(self, name, price):
        self.price = price
        self.name = name


cart = ShoppingChart()
cart.add(CartItem("Tesla", 100000))
cart.add(CartItem("Leaf", 30000))

for item in cart:
    print("* ${:,} - {}".format(item.price, item.name))

print("The total is {}".format(cart.total))