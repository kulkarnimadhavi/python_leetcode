# python 3 program to find multiplication
# of two number without use of
# multiplication operator
#if multiplier is odd , use shift operator by 2
# if the multipler is even , just divide the multiplier by 2


# Function for multiplication
def multiply ( n, m ) :
    ans = 0
    count = 0
    while (m) :
        # check for set bit and left
        # shift n, count times
        print("value of m is", m)
        if (m % 2 == 1) :
            ans += n << count
            print ("value of ans is ", ans)

            # increment of place value (count)
        count += 1
        print ("value of count is", count)
        m = int (m / 2)
        print ("value of m is", m)

    return ans


# Driver code
if __name__ == '__main__' :
    n = 20
    m = 13
    print (multiply (n, m))

# This code is contributed by
# Ssanjit_Prasad
