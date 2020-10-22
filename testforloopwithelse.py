def forloopwithelse():
    edibles = ["bacon", "eggs", "nuts"]
    for food in edibles:
        if food == "spam":
            print("No more spam please!")
            break
        print("Great, delicious " + food)
    else:
        print("I am so glad: No spam!")
    print("Finally, I finished stuffing myself")

#binary search for searhing a no. in the sorted list. logn almost half the lienar search
#bisect package


if __name__ == "__main__" :
    forloopwithelse()


