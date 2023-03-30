dictionary1 = {'a': 100, 'b': 400, 'c': 1000}
set4 = set(dictionary1)
print(set4)
set4.add(5)
print(set4)

print(set4.issubset(set4))

set5 = {'a', 'b', 'c', 'd', 'e'}
print(set5)
set5.discard(input("Enter a letter in the set to discard from it. "))
print(set5)

set6 = {1, 2, 3}
set7 = frozenset([1, 2, 3, 4])
print(set6)
print(set7)
