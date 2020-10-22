import json
import re
import time
import subprocess

def missingnointhearray():
  # input = [4,3,5,1,2,7]
  # print ("input the array with missing no")
   input1  = input("input the array with missing no")
   #input =input1
   sum_of_elements = sum(input1)
   print (sum_of_elements)
   n=len(input1)+1
   actual_sum = (n*(n+1))/2
   print("hi")
   print (actual_sum)
   missing_no = actual_sum-sum_of_elements
   print(missing_no)
   return missing_no

if __name__ == "__main__":
    missingnointhearray()
