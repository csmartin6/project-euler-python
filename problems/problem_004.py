palindromes = [x*y for x in xrange(900,1000) for y in xrange(900,1000) if str(x*y) == str(x*y)[::-1]]

print max(palindromes)