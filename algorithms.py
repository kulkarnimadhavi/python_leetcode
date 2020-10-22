#binary search for searhing a no. in the sorted list. logn almost half the lienar search
#bisect package
# Python code to demonstrate working
# of binary search in library
from bisect import bisect_left
from bisect import bisect_right
def binary_search(list1,x):
    i=bisect_right(list1,x)
    print(i)
    if i != len(list1) and list1[i] ==x:
        return i
    else:
        return -1

    #print(i)

#buble sort - swaps adjacent elements
def bublesort(list):
    temp=0
    for j in range(0, len(list)-1):
        for i in range(0,len(list)-1):
            if list[i] > list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
    print(list)


def pascalsTriangle(num):
    list=[[1]]
    if num ==1:
       return(list)
    else:
        temp=[1]
        for i in range(0, num-1):
            temp= createlisttoflist(temp)
            list.append(temp)
    return(list)


def createlisttoflist(list1):
    list2=[]
    if len(list1) == 1:
        list2=[1,1]
        return(list2)
    list2.append(1)
    for i in range (0, len(list1)-1):
        list2.append(list1[i]+list1[i+1])
    list2.append(1)
    return(list2)







if __name__ == "__main__":
    #list = [1,2,1]
    #num =1
    #list1 =sorted(list)
    #print(list1)
   # binary_search(list1,7)
   # bublesort(list)
   print(pascalsTriangle(3))
    #createlisttoflist(num)