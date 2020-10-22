#have the peoples name and birthdate and display people with same birthdays
import time
import datetime


"""
people with sdame bd
"""
def findpeople():
    date1 = datetime.date.today()
    date2 = datetime.date(2020,8,07)
    stored_names= {}
    dict= {"5/12/1990":"kate bose","5/11/1990":"neil bose","5/12/1992":"anita bose","3/1/1980":"vinita bose"}
    #compare_dates(dict)
    keys = dict.keys()
    #print(keys)
    for i in range(0,len(keys)):
        for j in range(i+1,len(keys),1):
            print("i=",i)
            print("j=",j)
            key1 = keys[i]
            key2= keys[j]
            print(key1, key2)
            if key1 != key2:
                if compare_dates(key1,key2):
                    stored_names[key1]= dict[key1],dict[key2]
                    #print(stored_names)


def strdate(str):
    return str.split("/")

def compare_dates(key1, key2):
    key1_split = strdate(key1)
    key2_split = strdate(key2)
    if key1_split[0] == key2_split[0] and key1_split[1]==key2_split[1]:
        #print(key1_split[0]+'/'+key1_split[1])
        matched_key = key1_split[0]+'/'+key1_split[1]
        #print(matched_key)
        return True
    return False


if __name__ == "__main__" :
        #compare_dates("4/12/1990", "4/12/1980")
        findpeople()