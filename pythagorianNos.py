from math import sqrt
def pythagorianNos(n):
    #n = input("Maximum Number? ")
    n = int(n)+1
    for a in range(1,n):
        for b in range(a,n):
            print("a==")
            print(a)
            print("b==")
            print(b)
            c_square = a**2 + b**2
            c = int(sqrt(c_square))
            if ((c_square - c**2) == 0):
                print(a, b, c)

if __name__ == "__main__":
    pythagorianNos(3)
