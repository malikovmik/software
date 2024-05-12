def merge_unique(list1, list2):
    unique_elements = set(list1) | set(list2)
    return list(unique_elements)

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
print(merge_unique(list1, list2))

tuple1 = (1, 2, 3)
tuple2 = (3, 4, 5)
print(merge_unique(tuple1, tuple2))

list3 = ['apple', 'banana', 'cherry']
list4 = ['banana', 'date', 'elderberry']
print(merge_unique(list3, list4))
