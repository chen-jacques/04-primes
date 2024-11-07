"""prints primes numbers from 0 to 100"""

from math import sqrt


#### Fonction secondaire


def isprime(p):

    """return if number is prime"""
    # votre code ici
    if p in (1,0):
        return False
    for i in range (2, int(sqrt(p))+1):
        if p%i==0:
            return False
    return True

#### Fonction principale


def main():

    """body of the code"""
    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
