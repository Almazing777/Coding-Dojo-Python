class Product(object):
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"

    def display_info(self):
        print self.price, self.item_name, self.weight, self.brand, self.status

    def sell(self):
        self.status = "sold"
        return self

    def tax(self):
        tax = decimal * self.price
        self.fullprice = tax + self.price
        return self

    def item_return(self, reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
            return self
        if reason == "returned in box":
            self.status = "for sale"
            return self
        if reason == "box opened":
            self.status = "used"
            self.price *=0.80
            return self

product1 = Product(200, "console", 15, "xboxone")
product1.display_info()

product2 = Product(220, "console", 15, "ps4")
product2.display_info()
