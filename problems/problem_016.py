from ..projectEulerUtils import projectEulerUtils as utils
N=1000

digits= [1]

for i in xrange(N):
	digits=utils.addDigitArray(digits,digits)

print sum(digits)