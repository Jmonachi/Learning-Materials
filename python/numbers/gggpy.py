def _count_change(money, ways, n=0):
    if money == 0:
        return 1
    elif money < 0:
        return None
    else:
        t = 0
        for n in range(n, len(ways)):
            coin = ways[n]
            if money - coin < coin:
                b = _count_change(money - coin, ways, n+1)
            else:
                b = _count_change(money - coin, ways, n)

            if b:
                t += b
        return t

def count_change(money, ways):
    return _count_change(money, ways)

print(_count_change(4, [1, 2]))