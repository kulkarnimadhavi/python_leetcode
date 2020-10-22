import json
import re
import time
import subprocess


def fibonci(n):
    if n < 0:
       print("negative no")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonci(n-1)+fibonci(n-2)

print (fibonci (9))




    #if __name__ == "__main__":
    #print(fibonci(7))
