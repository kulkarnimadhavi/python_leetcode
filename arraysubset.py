"""
verify s2{5,8,2} is a subset of of S1{1,5,4,6,8,1} and not a subset of s3 {5,8,2,7}
"""
def arraysubset():
    s1 = {1,5,4,6,8,2}
    s2 = {5,8,2}
    s3 = {5,8,2,7}
    s4 = s1 | s2
    s5 = s1 | s3

    if ((s3 & s2 ) == s2 ):
        print("s2 is subset of s1")
    if (s1 ^ s3 != 0):
        print("s3 is not a subset of s1")

if __name__ == "__main__" :
    arraysubset()
