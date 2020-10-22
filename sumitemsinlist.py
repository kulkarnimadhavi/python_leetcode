import math
from random import shuffle
def sumitemsinlist():
    list =[4,3,2,1,5,7]
    sum=0
    for element in list:
        sum = sum+element
    print("hi")
    print(sum)

def mulitplyitemsinlist():
    list=[3,2,1,3,0,2]
    answer =1
    for element in list:
        if element != 0:
            answer = answer *element
        print(answer)

def largestno():
    list=[2,12,5,3,9]
    max=list[0]
    for item in list:
        if max < item:
            max =item
    print(max)


def findstring():
    list=['abca','nm', 'cvxz', 'asda', 'rtey', 'lkjl', 'asdfgha', 'aa', 'asdasda', 'ere']
    count = 0
    for item in list:
        if len(item) >2:
            if item[0] == item[len(item)-1]:
                    count+=1
    print(count)


def last(n): return n[-1]

def sort_list_last(tuples):
    return sorted(tuples, key=last)

#print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))


def removeduplicates():
    list=[1,'a', 4, 1, 9, 'a']
    dup_items = set()
    modlist=[]
    for element in list:
        if element not in dup_items:
            modlist.append(element)
            print("modlist in loop",modlist)
            dup_items.add(element)
            print("dup-list in loop", dup_items)
    print(modlist)


def listempty():
    list=[]
    if len(list) ==0:
        print("empty list")


def findwords():
    listgiven=["this" , "is", "python", "excercise" , "from", "the", "web"]
    listfound=[]
    for word in listgiven:
        if (len(word) <=4):
            listfound.append(word)
    print(listfound)


def modifiedlist():
    SampleList= ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    x=0
    SampleList = [x for (i, x) in enumerate(SampleList[x]) if x not in (0,4,5)]
    #print("i==", i)

    print(SampleList)

def printoddnos():
    list=[1,2,3,4,5,6,7,8,9]
    listeven=[]
    for element in list:
        if element % 2 != 0:
            listeven.append(element)
    print(listeven)

def shufflelist():
    list=[1,2,3,4,5,6,7]
    shuffle(list)
    list1=[]
    for i in range (len(list), 0, -1):
        list1.append(i)
    print(list)

def sqrtofnos():
    list=[]
    list1=[]
    x=0
    for i in range(1,1000):
        if math.sqrt(i).is_integer():
            if math.sqrt(i) <= 30:
                list.append(i)
    if len(list) >= 6:
        print("doing nothing")
        list =list[1:25]
        #list = [x for (i, x) in enumerate(list[x]) if x not in (1,26,27,28,29,30)]
    print(list)



if __name__ == "__main__":
    #sumitemsinlist()
     #mulitplyitemsinlist()
     #largestno()
     #findstring()
     #sort_list_last()
     #removeduplicates()
     #listempty()
     #findwords()
     #modifiedlist()
     #printoddnos()
     #shufflelist()
     sqrtofnos()
