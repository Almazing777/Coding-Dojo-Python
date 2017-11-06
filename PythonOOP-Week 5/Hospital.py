class Patient(object):
    id = 0
    bed_num = 0
    def __init__(self, name, allergies):
        self.name = name
        self.allergies = allergies
        self.id = Patient.id
        self.bed_num = Patient.bed_num
        Patient.id += 1
        Patient.bed_num += 1

    def info(self):
        print self.name
        print self.allergies
        print "ID: {}".format(self.id)
        print "Bed No. {}".format(self.bed_num)

patient1 = Patient("John Smith","Peanuts")
patient1.info()

patient2 = Patient("Adam Smith", "Animal Allergy")
patient2.info()


class Hospital(object):
    def __init__(self, name, capacity=10, patients=[]):
        self.patients = patients
        self.name = name
        self.capacity = capacity

    def add(self, patient):
        if len(self.patients) > self.capacity:
            print "Max. capacity reached"
            return self
        else:
            self.patients.append(patient)
            print "New Patient is admitted "
            return self

    def remove(self, patient):
        for i in self.patients:
            if i == patient:
                patient.bed_num = 0
                self.patients.remove(patient)
                print "patient {}".format(i.name)+" discharged"
                return self

    def hospital_info(self):
        print self.name
        print "capacity is {}".format(self.capacity)


hospital = Hospital('Inova')
hospital.add(patient1).add(patient2).remove(patient1).hospital_info()


# class Call(object):
#     uniqueID = 0
#     def __init__(self, name, phone_num, reason):
#         self.id = id
#         self.name = name
#         self.phone_num = phone_num
#         self.time = datetime.now()
#         self.reason = reason
#         Call.uniqueID += 1
#
#     def display_all(self):
#         print self.id
#         print self.name
#         print self.phone_num
#         print self.time
#         print self.reason
#
# caller1 = Call("Almas", 7038390891, "appointment")
# caller1.display_all()
#
# caller2 = Call("Aliya", 7038390890, "customer service")
# caller2.display_all()
#
#
# class CallCenter(object):
#
#     def __init__(self):
#         self.calls = []
#         self.queue_size = 0
#
#     def add(self, call):
#         self.calls.append(call)
#         return self
#
#     def remove(self, call):
#         self.calls.remove(self.calls[0])
#         return self
#
#     def info(self):
#         print self.calls
#         print self.queue_size
#         return self
#
# callcenter = CallCenter()
# callcenter.add(caller1).add(caller2).info()




