import projectEulerUtils
N=1000

digits= [1]

for i in xrange(N):
	digits=projectEulerUtils.addDigitArray(digits,digits)

print sum(digits)