def answer(minion_num, limit=20231):
    #  my variation of Sieve of Eratosthenes example from RosettaCode
    is_prime = [False] * 2 + [True] * (limit - 1)
    for n in range(int(limit**0.5 + 1.5)):
        if is_prime[n]:
            for i in range(n*n, limit+1, n):
                is_prime[i] = False
    return "".join([str(i) for i, prime in enumerate(is_prime) if prime])[minion_num:minion_num+5]


assert answer(0) == "23571"
assert answer(3) == "71113"
