import re
"""
Abstract: This module finds the phrase in the sentence and prints whether the match exists or not
"""
def searchphrase():
    """Function uses regex re to find whether the sentence has the phrase
    """
    sentence = "I want to be a full automation engineer"
    phrase= "full automation"
    if re.search(phrase,sentence):
        print("sentence contains the phrase")
        result = re.search(phrase,sentence)
        print (result.group())
    else:
        print("no match")

if __name__ == "__main__":
    searchphrase()