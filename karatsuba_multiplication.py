__author__ = 'Ramon'


def karatsuba(x, y):
    xl = list(str(x))
    yl = list(str(y))

    # base case
    if len(xl) <= 2 or len(yl) <= 2:
        return x*y
    else:
        while (len(xl)/2) % 2 != 0:
            x *= 10
            xl = list(str(x))
        while (len(yl)/2) % 2 != 0:
            y *= 10
            yl = list(str(y))

        # if x and y have different lenght
        if len(xl) > len(yl):
            y *= 10**(len(xl)/len(yl))
        #    yl = list(str(y))  # no hay necesidad de hacer esto pq len(xl) = len(yl)
        elif len(xl) < len(yl):
            x *= 10**(len(yl)/len(xl))
            xl = list(str(x))

        n = len(xl)

        a = int(x/(10**(n/2)))
        b = int(x % (10**(n/2)))   # tomando el resto
        c = int(y/(10**(n/2)))
        d = int(y % (10**(n/2)))   # tomando el resto

        step1 = karatsuba(a, c)
        step2 = karatsuba(b, d)
        #step3= karatsuba(a, d) + karatsuba(b, c) + step1 + step2
        step3 = karatsuba(a+b, c+d)

        # Gauss's trick
        gt = step3 - step1 - step2

        return (10**n)*step1 + (10**(n/2))*gt + step2


print(karatsuba(1234,5678))