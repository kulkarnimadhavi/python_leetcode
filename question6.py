#https://www.python-course.eu/python3_decorators.php
def call_counter ( func ) :
    def helper ( x ) :
        print(x)
        helper.calls += 1 #question where the object helper is defined ?n helper.calls calls attribute ??? where is it comin from
        return func (x)

    helper.calls = 0

    return helper


@call_counter
def succ ( x ) :
    return x + 1


print (succ.calls)
for i in range (10) :
    succ (i)

print (succ.calls)