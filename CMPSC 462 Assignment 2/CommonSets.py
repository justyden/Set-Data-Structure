def commonSet(set1, set2):
    return set1.symmetric_difference(set2)


set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7, 8, 9, 10}

set3 = commonSet(set1, set2)
print("The unique numbers within the sets are - " + str(set3))
