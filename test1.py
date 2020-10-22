# in a sentence , find the occurance of each character
# find the length , len-1 use the loop for the range 1-len-1 and compare the
# letter is digit or character
# list and 26 items -
# lower the
# exceptiuon for other than letters fo findindex -if there is a number
# dictionary approach - and try -catch ,global variable for 26-

def find_occurance () :
    sentence = "I am using python3 in pycharm"
    mylist = []
    for i in range (0, 26) :
        mylist.append (0)
    for letter in sentence :
        if letter.isalpha ( ) :
            index = findindex (letter)
            mylist[index] += 1
    return mylist


def findindex ( letter ) :
    # given a letter it should be able to return an index
    # index =0
    if letter.islower ( ) :
        letter_index = ord (letter) - ord ('a')
    else :
        # print(ord(letter)-ord('A'))
        letter_index = ord (letter) - ord ('A')
    return letter_index


# print the letters with the occurances
def print_letters_occurances ( mylist ) :
    start = ord ('a')
    for i in range (0, 26) :
        letter = chr (start + i)
        if mylist[i] > 0 :
            print (letter, "-", mylist[i])


# use dictionary
def findletteroccurances ( sentence ) :
    sentence = (sentence.lower ( )).replace (" ", "")
    print (sentence)
    length = len(sentence)
    mydict = {}
    j = 0
    for letter in range(0,length) :
        for key in mydict :
            if key == letter :
                j += 1
                length-=length
                mydict.update ({letter : j})
            else :
                j = 0
    # sort the dictionary on keys
    print (mydict)


if __name__ == "__main__" :
    sentence = "need to find the sorted dictionary"
    findletteroccurances (sentence)
    # letter_occurance =find_occurance()
# print_letters_occurances(letter_occurance)
