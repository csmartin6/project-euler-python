import math

N=1000
fib=[1,1]
i = 1
digits = 1

while (digits < N) :
	fib.append(fib[i]+fib[i-1])
	i+=1 
	digits = int(math.log10(fib[i]))+1

print (i+1)