def _answer(n, result):
    ans = int(n ** .5) ** 2
    result.append(ans)
    n = n - ans
    if n == 0:
        return result
    else:
        return _answer(n, result)


def answer(n):
    squares = [x ** 2 for x in range(1, 1001)]
    if n in squares:
        return [n]
    else:
        return _answer(n, [])
