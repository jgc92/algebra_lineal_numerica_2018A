def sieve(n):
    """Holas ntehuneohu
netuhneohunteo
eohunteohuntheou
ntheuntheontuh"""
    ns = []
    primes = []
    
    for i in range(2, n+1):
        if i not in ns:
            primes.append(i)
            for j in range(i*i, n+1, i):
                ns.append(j)

    return primes

print(sieve(100))
