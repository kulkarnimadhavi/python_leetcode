def find_sum_of_two(A, val):
    found_values=set()
    for a in A:
        if val-a in found_values:
            return True
            temp =a
            found_values.add (a)
            print (found_values)
            return True


    return False

if __name__ == "__main__":
    find_sum_of_two([1,3,4,5,7], 8)