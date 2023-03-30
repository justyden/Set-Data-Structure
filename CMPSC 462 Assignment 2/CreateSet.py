# Prompt the user to input two sets and display some useful information about both sets.

def createSet():
    userInput1 = input("Enter the elements for set 1 seperated by commas - ")
    set1 = set(userInput1.split(','))
    userInput2 = input("Enter the elements for set 2 seperated by commas - ")
    set2 = set(userInput2.split(','))

    print("Here is set 1 - " + str(set1))
    print("Here is set 2 - " + str(set2))

    if set1.issubset(set2):
        if set2.issubset(set1):
            print("They are both a subset of the other.")
        else:
            print("Set 1 is a subset of set 2.")
    elif set2.issubset(set1):
        print("Set 2 is a subset of set 1.")
    else:
        print("Neither set is a subset of the other set.")

    if set1.issuperset(set2):
        if set2.issuperset(set1):
            print("They are both a super set of the other.")
        else:
            print("Set 1 is a supersset of set 2.")
    elif set2.issuperset(set1):
        print("Set 2 is a superset of set 1.")
    else:
        print("Neither set is a superset of the other set.")

    print("Here is the union of both sets - " + str(set1.union(set2)))

    print("Here is the intersection of the sets - " +
          str(set1.intersection(set2)))

    print("Here is set 1 with the difference of set 2 - " +
          str(set1.difference(set2)))

    print("Here is set 2 with the difference of set 1 - " +
          str(set2.difference(set1)))


createSet()
