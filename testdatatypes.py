"""
list program

"""
list=["hello",2,3]
for element in list:
    print (element)

list=[]
for i in range(1,10,1):
    list.append(i)
print(list)

dict={2:"hello", 3:"hi"}
list=[]
for key in dict:
    print(key)

for i in dict.keys():
    print(i)

for i in dict.values():
    print(i)
list1=[]
list2 =[]
for word in dict.items():
    print(word)
    list1.append(word[0])
    list2.append(word[1])

A=(1,"Hello")
print(A[0])


sentence ="abcdefg"
for letter in sentence:
    print(letter)

sentence = "this- is- python"
for letter in sentence:
    print(letter)
for word in sentence.split("-",1):
    print(word)
    print(len(word))
for word in (sentence.split("-")):
    print(word.split())

 #input/output

#A = input("enter A=")
#print(A)
#A=int(A)+1
#A = A+"hello"
#print(A)
print("%d %2.3f" %(2,3))
#print("A=",10,"B=",20)

A=(1,"Hello")
B=(2, "python")
.....
print(A[0])
print(A[1])
