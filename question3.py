def f () :
    city = "Hamburg"

    def g () :
       global city   ##"scope of this ??"
       city = "Geneva"

    print ("Before calling g: " + city)
    print ("Calling g now:")
    g ( )
    print ("After calling g: " + city)


f ( )
print ("Value of city in main: " + city)