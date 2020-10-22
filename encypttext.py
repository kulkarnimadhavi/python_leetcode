##Write a function which takes a text and a dictionary to decrypt or encrypt the given text.
def encrpyt(test, **testdict):
    print(test)
    print(testdict)


if __name__ == "__main__" :
    test ="rainyday"
    testdict = {1:"sun", 2:"rain"}
    encrpyt(test,testdict)