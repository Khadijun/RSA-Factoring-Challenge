#!/usr/bin/python3
import math


def factors():
    numbers = [4, 12, 34, 128, 10244958, 1718944270642558716715, 9, 99,
               999, 9999, 9797973, 49, 239809320265259]
    for n in numbers:
        q = math.isqrt(n)
        for p in range(2, q + 1):
            if n % p == 0:
                q = n // p
                print("{}={}*{}".format(n, p, q))
                break


factors()
