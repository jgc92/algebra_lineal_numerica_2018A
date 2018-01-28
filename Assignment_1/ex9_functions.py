def sieve(n: int) -> [int]:
    """ Sieve of Eratosthenes algorithm.

        Args:
            n: range of the sieve.

        Returns:
            List of primes numbers up to n.
    """
    ns = []
    primes = []
    
    for i in range(2, n+1):
        if i not in ns:
            primes.append(i)
            for j in range(i*i, n+1, i):
                ns.append(j)

    return primes
