arr1 = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
arr2 = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(arr1, arr2):
  while len(arr1) == len(arr2):
    print "lists are equal"
  else:
    print "lists are not equal"

new_dict = dict(zip(arr1, arr2))
print new_dict
