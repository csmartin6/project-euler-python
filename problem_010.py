
import numpy as np
N=2000000

acc = 2
nums = xrange(3,N+1,2)
cur_prime = 3
while cur_prime <= np.sqrt(N):
	cur_prime = nums[0]
	acc += cur_prime
	nums = [x for x in nums if x%cur_prime!=0]

result = acc + sum(nums)
print result