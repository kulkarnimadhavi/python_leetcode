def mergelist_sortlist(list1, list2):
    list1.extend(list2)
    print(sorted(list1))
    return(list1)


def find_array_degree(list1):
    """
    An array that has degree d, must have some element x occur d times. If some subarray has the same degree, t
    hen some element x (that occured d times), still occurs d times. The shortest such subarray would be
    from the first occurrence of x until the last occurrence.

    For each element in the given array, let's know left, the index of its first occurrence; and right,

    the index of its last occurrence. For example, with nums = [1,2,3,2,5] we have left[2] = 1 and right[2] = 3.

    Then, for each element x that occurs the maximum number of times, right[x] - left[x] + 1 will be our candidate answer,
    and we'll take the minimum of those candidates.
    """
    temp_count=0
    #dict_of_count = {element:[left_count,right_count]}
    dict_of_count ={}
    temp_count =0
    element =0
    for element in list1:
        if element in dict_of_count:
            dict_of_count[element]= dict_of_count[element]+1
        else:
            dict_of_count[element]=1
    return(max(dict_of_count.values()))


def find_subarray(list1,degree):
    #list1 = [1, 2, 3, 4, 2, 9, 3, 1]
    subarray=[]
    #degree =2
    j=degree
    for j in range (degree, len(list1)):
        for i in range(0, len(list1)-j+1):
            subarray =list1[i:i+j:1]
            #print(subarray)
            if find_array_degree(subarray) == degree:
                return(subarray)



def square_of_digits(num,counter):
    if num == 1:
        print("num is the happy number", num)
        return
    if counter == 10:
        print("not a happy no")
        return
    sum=0
    j=0
    while num != 0:
        rem= num % 10
        sum = sum + rem * rem
        num = int(num / 10)
    counter = counter-1
    return square_of_digits(sum)

def no_in_words(no):
    number= no.split(no, ",")
    length = len(number)
    dict = {}
    #write a function given the last 3 digits tell the no. mod10


def print_digits(number)












if __name__ == "__main__":
    list1= [1,2,3,4,2,9,3,1]
    list2 =[1,6,5,2,9]
    no= "1,234,123"
    no_in_words(no)
   # mergelist_sortlist(list1,list2)
    #degree =find_array_degree(list1)
    #print(find_subarray(list1,degree))
    #print(square_of_digits(9,10))







