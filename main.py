import utils

if name == "__main__":
    print("Факторіал числа 5:", utils.factorial(5))


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
