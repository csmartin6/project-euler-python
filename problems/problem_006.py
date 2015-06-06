N = 100
sum_of_squares = 0;
for i in xrange(N+1):
	sum_of_squares += i*i
	
#sum_of_squares = reduce(lambda acc,x: acc+x*x, range(N+1))
squared_sum = (N*(N+1)/2)**2
result = squared_sum-sum_of_squares
print result