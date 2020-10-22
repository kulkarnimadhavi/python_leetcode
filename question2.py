class Fibonacci :

    def __init__ ( self, i1=0, i2=1 ) :
        self.memo = {0 : i1, 1 : i2}

    def __call__ ( self, n ) :
        if n not in self.memo :
            self.memo[n] = self.__call__ (n - 1) + self.__call__ (n - 2)
        return self.memo[n]


fib = Fibonacci ( )
lucas = Fibonacci (2, 1)  ##1)===>what is the lucas fuction is doing here?? 2) how is it referring to fibbonci and still having the different results?3) __call__ how is it hiding a dictionary?



for i in range (1, 16) :
    print (i, fib (i), lucas (i))