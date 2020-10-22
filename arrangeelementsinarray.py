"""
arrange the array starting with a positive no. and alternate pos , neg.and pos sorted
assending and neg sorted assending
"""
def arrangearray():

    """
     *keep a list for pos sorted
     *keep a list for negative sorted
     *merge the list s
    """
    list_given=[ -1,6,9,-4,-10,-9,8,8,4]
    list_pos=[]
    list_neg=[]
    for el in list_given:
        if el >= 0:
            list_pos.append(el)
        else:
            list_neg.append(el)
    #sort the arrays
    list_pos.sort()
    list_neg.sort()

    #Merge the pos array and neg array starting positive array
    for i in range(len(list_pos)):
        for j in range(len(list_neg)):
            if i==0:
                list_given[i] = list_pos[i]
            elif i % 2== 0 :
                list_given[i] = list_pos[i]
            else:
                list_given[j] = list_neg[j]
    #special cases of if positive array is larger append all
    print(list_given)
    res_list= zip(list_pos, list_neg)

    print(list(res_list))


if __name__ == "__main__" :
    arrangearray()

