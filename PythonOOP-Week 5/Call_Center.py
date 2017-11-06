from datetime import datetime

class Call(object):
    uniqueID = 0
    def __init__(self, name, phone_num, reason):
        self.id = id
        self.name = name
        self.phone_num = phone_num
        self.time = datetime.now()
        self.reason = reason
        Call.uniqueID += 1

    def display_all(self):
        print self.id
        print self.name
        print self.phone_num
        print self.time
        print self.reason

caller1 = Call("Almas", 7038390891, "appointment")
caller1.display_all()

caller2 = Call("Aliya", 7038390890, "customer service")
caller2.display_all()


class CallCenter(object):

    def __init__(self):
        self.calls = []
        self.queue_size = 0

    def add(self, call):
        self.calls.append(call)
        return self

    def remove(self, call):
        self.calls.remove(self.calls[0])
        return self

    def info(self):
        print self.calls
        print self.queue_size
        return self

callcenter = CallCenter()
callcenter.add(caller1).add(caller2).info()




