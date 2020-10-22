def searchstring():
    sentence = input ("enter the sentence")
    length = len(sentence)
    search = input("enter the string to search\n")
    if len(sentence)== 0 :
        print("emnpty sentence")
    sentenceList = sentence.split()
    for word in sentenceList:
        if (search in word) :
            print ("found the match")


def findstring():
    sentence = "I am learning python"
    search="learning"
    result = sentence.find(search)
    print (result)



if __name__ == "__main__":
    searchstring()
    #findstring()
