import utils

if name == "__main__":
    print("Факторіал числа 5:", utils.factorial(5))


def gcd(b, a):
    while a:
        b, a = a, b % a
    return b
