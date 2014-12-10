import time

N = 1000001
seq_lengths = {}

def nextNum(n):
	next_number =  n/2 if (n%2 == 0) else 3*n+1
	return next_number


t0 = time.time()
seq_lengths[1]=1

for i in xrange(2,N):
	current_number = i
	count = 0
	while current_number not in seq_lengths:
		current_number = nextNum(current_number)
		count+=1

	seq_lengths[i]=count+seq_lengths[current_number]

print max(seq_lengths, key=lambda k: seq_lengths[k])
t1 = time.time()
print "Elapsed time: "+str(t1-t0)

