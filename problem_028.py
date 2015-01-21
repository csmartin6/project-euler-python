N = 1001
s = 1 
for a in xrange(3,N+1,2):
	corners = range(a*a,(a-2)*(a-2),-a+1)
	s += sum(corners)


print s 
