# pumped_up = False
# def pump():
# 	ball = "basketball"
# 	print "pumping air"
# 	print "done pumping"
# 	def deflate():
# 		print "deflating a ball"

# pump("hand","basketball")
# print pumped_up

#Foo bar 

for x in xrange(100,1000):
	print x
	square = False
	for i in xrange(10, x):
		if i*i == x:
			print "perfect square"
			break
		elif i*i > x:
			print "not a perfect square"
			break

	if square == False:
		prime = True
		for i in xrange( 2, x/2):
			if x % 1 == 0:
				prime = False
				break
		if prime == True:
			print 'prime'
