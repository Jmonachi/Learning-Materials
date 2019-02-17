def ordinal( x ):

    suffix = ['th', 'st', 'nd', 'rd', 'th', 'th', 'th', 'th', 'th', 'th']

    if x < 0:
        x *= -1

    x = int(x)

    if x % 100 in (11,12,13):
        p = 'th'
    else:
        p = suffix[x % 10]

    return str(x) + p

print[ordinal(n) for n in range(1,10)]

