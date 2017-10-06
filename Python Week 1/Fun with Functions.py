def odd_even():
    for x in range (1, 2001):
        if x % 2 == 0:
            print "this is an even number", [x]
        else:
            print "this is an odd number", [x]
print odd_even()



def multiply(arr, num):
    for x in range (len(arr)):
        arr[x]*= num
    return arr
a=[2,4,10,16]
b=multiply(a,5)
print b

def layered_multiples(arr):
  new_array = []
  for x in arr:
      val_arr = []
      for x in range (0,x):
          val_arr.append(1)
          new_array.append(val_arr)
  return new_array
x = layered_multiples(multiply([2,4,5],3))
print x