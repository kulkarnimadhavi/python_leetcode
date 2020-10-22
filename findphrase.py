#find the phrase in the sentence
#kmb algorithm
#find a function if there is a string in a sentence
"""
find the string in a sentence

"""
def findword(sentence, word):
    i=0
    letter=""
    for j in range(0, len(sentence)):
        letter=sentence[j]
        if word[i] == letter:
            if positionsentence (word, sentence, j):
                print("test passed")
                return True
    return False

"""
find the string in a sentence

"""
def positionsentence( word,sentence,start):
    i=0
    for j in range(start,len(sentence)):
        letter=sentence[j]
        if word[i] == letter :
            print ("letter=", letter)
            print ("word[i]", word[i])
            i += 1
            if i == len (word) :
                return True
        else :
            i = 0
    return False




def findphrase():
    sentence = "this is fun project to do with python"
    phrase ="fun project"
    if sentence.find("phrase"):
        print("substring present")



if __name__ == "__main__":
    sentence = "This is ffun project rake project"
    word = "fun project"
    if findword(sentence, word):
        print("test passes")
