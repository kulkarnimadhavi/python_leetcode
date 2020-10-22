"""
test to find if the two strings are anagram
"""
def findanagram():
    """
    take the strings and find the length is equal.If it is call the function to check the
    characters match
    """
    str1 = "LISTEN"
    str2= "SILENT"
    if len(str1)==len(str2):
        if findcharmatch(str1, str2):
            print("the strings are anagrams")
        else:
            print("not an anagram")


def findcharmatch(str1,str2):
    """
     compare two equal length strings and returns true if they have same characters
     @param str1: string
    @param str2: string
    @return: bool
    """
    result = False
    for element in str1:
        if element in str2:
            result = True
        else:
            result= False
            break
    return(result)


if __name__ == "__main__" :
    findanagram()