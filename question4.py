#https://www.python-course.eu/python3_decorators.php functions returning functions do not get the flow
def f(x):
    #print("in functionx print x")
    #print(x)
    def g(y):
        #print("in function g print x")
        #print(x)
       # print("in function g print y")
       # print(y)
        return y + x + 3
    return g


#print("before nf1")
nf1 = f(1)
#print("after nf1")
nf2 = f(3)
#print("after nf2")

print(nf1(1))
print(nf2(1))


#if __name__ == "__main__" :
