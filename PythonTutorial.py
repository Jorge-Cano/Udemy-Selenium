a = "NYC"
b = "Austin"
distance = "1,599"

print(a + " is your starting point.")
print (b + " is your destination point")
print ("The total distance from " + a + " to " + b + " is approxmiately " + distance + " miles.")

for x in xrange(3):
    print x
else:
    print 'Final x = %d' % (x)

for x in xrange(3):
    if x == 1:
        break
