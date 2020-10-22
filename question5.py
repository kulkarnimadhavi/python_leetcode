def decorator1(f):
    def helper():
        print("Decorating", f.__name__)
        print("before f")
        print(helper)
        f()
        print("after f")
        print("helper")
        print(helper)
    return helper

print (factorial (-1))

@decorator1
def foo():
    print("inside foo()")

foo()