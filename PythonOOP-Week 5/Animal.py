class Animal(object):
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        print "walking"
        return self

    def run(self):
        self.health -= 5
        print "running"
        return self

    def display_health(self):
        print "Health remaining:", self.health
        print "---------------------------"


animal1 = Animal("Horse", 100)
animal1.walk().walk().walk().run().run().display_health()


class Dog(Animal):
    def __init__(self):
        super(Dog, self).__init__("Sparky", 150)

    def pet(self):
        self.health += 5
        return self

sparky = Dog()
sparky.walk().walk().walk().run().run().pet().display_health()

class Dragon(Animal):
    def __init__(self):
        super(Dragon, self).__init__("Wyvern", 170)

    def fly(self):
        self.health -= 10
        print "flying"
        return self

    def display_health(self):
        print "Health remaining:", self.health
        print "I'm Dragon"
        print "---------------------------"

wyvern = Dragon()
wyvern.fly().fly().display_health()

class Rabbit(Animal):
    def __init__(self):
        super (Rabbit, self).__init__("Buggs Bunny", 200)

BB = Rabbit()
BB.run().run().run().display_health()