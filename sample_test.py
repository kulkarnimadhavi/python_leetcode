import pytest
def test_hello(hello, first_tc, third_tc):
    # Hi there
    print("This is my first test case")


def test_second(hello, first_tc, second_tc):
    print("This is my second test case")

@pytest.mark.usefixtures("third_tc")
def test_third():
    print("This is my third test")


def test_fourth(fourth_tc, fifth_tc):
    num1, num2 = fourth_tc

    print("\n Printing value returned bby fixture", num1)
    print("\n Printing value returned bby fixture", num2)
    print("\n printing last name", fifth_tc['ln'])


def test_six(sixth_tc):
    response = sixth_tc('Eddie')
    print("\n sixth test value", response)

def test_seven(seven_tc):
    print("\n sixth test value", seven_tc)


def test_eight(eight_tc):
    print("\n eighth test value", eight_tc)





@pytest.mark.parametrize(
    "test_input, expected",
    [("3+5", 8), ("2+4", 6)],
)
def test_nine(test_input, expected):
    print("\n Inside test nine")
    print("Input", test_input)
    print("Expected", expected)


def test_ten(A2ACalling):
    print("\n using yml file")
    print("input", A2ACalling['input'])
    print("output", A2ACalling['output'])


def test_11(B2BCalling):
    print("\n using yml file for second time")
    print("input", B2BCalling['input'])
    print("output", B2BCalling['output'])



#create a simple fixture in conftest and use it
def test_learn1(learn_conftest1):
    print("\n learn conftest")


#fixture calling another fixture
def test_learn2(learn_conftest2):
    print("\n fixure calling another fixture third_tc and third_tc calling second_tc")


#call more than one fixture --did not work
def test_learn3(learn_conftest2, second_tc):

    print("\n you can call 2 fixtures and they will execute one by one ")




def test_learn4(learn_conftest3):
    print("\n print from test that uses fixture with return and teardown add finalizer")
    month,day =learn_conftest3
    print(month)
    print(day)



def fibonci(n):
    if n < 0:
       print("negative no")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else
        return Fibnci(n-1)+fibonci(n-2)












