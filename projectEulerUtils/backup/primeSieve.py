
def primeSieve(N):
    pos_primes = [True] * N                         
    pos_primes[0] = pos_primes[1] = False
    for (i, isprime) in enumerate(pos_primes):
        if isprime:
            yield i
            for n in xrange(i*i, N, i):     
                pos_primes[n] = False
