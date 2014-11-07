fib = [1,1]
while(fib[-2]+fib[-1]<4000000):
	fib.append(fib[-2]+fib[-1])

answer = sum([x for x in fib if x % 2 == 0])

print answer