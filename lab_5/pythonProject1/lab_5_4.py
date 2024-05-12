def correction(arr):
    arr_correct = [elem for elem in arr if elem != 2]
    for index, elem in enumerate(arr_correct):
        if elem == 3:
            arr_correct[index] = 4
    return arr_correct

one = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
two = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
three = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

print(correction(one))
print(correction(two))
print(correction(three))
