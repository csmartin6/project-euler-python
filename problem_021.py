import projectEulerUtils

def properDivisors(x):
	divisors = projectEulerUtils.findDivisors(x)
	proper_divisors = sorted(divisors)[:-1]
	return proper_divisors

proper_divisor_sums = {}
amicable_pairs = set()
amicable_numbers = set()

N = 10001
for num in xrange(N):
	proper_divisor_sum = sum(properDivisors(num))
	proper_divisor_sums[num]=proper_divisor_sum
	
	if proper_divisor_sum in proper_divisor_sums:
		c_divisor_sum= proper_divisor_sums[proper_divisor_sum]		
	else:
		c_divisor_sum = sum(properDivisors(proper_divisor_sum))
		proper_divisor_sums[proper_divisor_sum] = c_divisor_sum

	if (num==c_divisor_sum) and num!=proper_divisor_sum:
		amicable_pair = (num,proper_divisor_sum) if num<proper_divisor_sum else (proper_divisor_sum,num)
		amicable_pairs.add(amicable_pair)
		
		amicable_numbers.add(num)
		amicable_numbers.add(proper_divisor_sum)

print amicable_pairs
print sum(amicable_numbers)
