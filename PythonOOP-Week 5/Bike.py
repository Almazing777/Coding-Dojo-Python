class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayinfo(self):
        print self.price, self.max_speed, self.miles

    def ride(self):
        self.miles +=10
        print "Riding"
        return self

    def reverse(self):
        if self.miles > 0:
            self.miles -=5
        print "Reversing"
        return self



bike1 = Bike(200, "25mph", 0)
bike1.ride().ride().ride().reverse().displayinfo()


bike2 = Bike(300, "30mph", 0)
bike2.ride().ride().reverse().reverse().displayinfo()

bike3 = Bike(400, "35mph", 0)
bike3.reverse().reverse().reverse().displayinfo()




