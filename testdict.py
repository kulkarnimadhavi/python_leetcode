import math
from random import shuffle

def sort_dict_byValue():
    dict={0:23, 1:12, 2:9, 3:6}
    min = dict[0]
    print(min)
    i=1
    print(sorted(dict.values()))
    print(sorted(dict.values(),reverse=True))


def sort_files():
    list=["a1.txt", "a2.txt", "a55.txt", "a53.txt","a10.txt"]
    #getnumber()
    print(sorted(list, key=getnumber))


def getnumber(str):
    #str = "a10.txt"
    nostr = str.split(".")
    number = nostr[0]
    digit=''
    for letter in number:
        if letter.isdigit():
            digit=digit+letter

    return int(digit)

def remove_key_from_the_dict():
    dict ={1:"the", 2:"python", 3:"remove", 4:"key"}
    dict.pop(3)
    print(dict)
    print(dict.)

    max(dict)
    print(max(dict))


def unique_dict_items():
    sample_dict = {"V": "S001", "V": "S002", "VI": "S001", "VI": "S005", "VIII": "S007"}
    set=()
    print(sample_dict.values())

def convert_list_to_values():
    list1=[[1,2],[3,4]]
    dict={}
    #sum=0
    for i in range(0, len(list1)):
        dict[i]=list1[i]
    for item in dict.values():
        print(sum(item))
        print(item)
    #print(dict.values())


    #print(dict)
    #print(sum)













if __name__ == "__main__":
    #sort_dict_byValue()
     #sort_files()
    #remove_key_from_the_dict()
    #unique_dict_items()
    convert_list_to_values( )