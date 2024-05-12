def transform_to_set(list):
    count = {}
    for elem in list:
        count[elem] = list.count(elem)
    result_set = set()
    for elem, value in count.items():
        result_set.add(elem)
        for i in range(2, value + 1):
            result_set.add(str(elem) * i)
    return result_set

list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

print(transform_to_set(list_1))
print(transform_to_set(list_2))
print(transform_to_set(list_3))
