N = 100
powers = set()
for a in range(2,N+1):
	cur = a
	for i in xrange(N-1):
		cur *= a
		powers.add(cur)
	 
print len(powers)







