def remove_fist_value(tuple, value):
    if value not in tuple:
        return tuple
    else:
        index = tuple.index(value)
        print(index)

        new_tuple = tuple[:index] + tuple[index+1:]
        return new_tuple


tuple1 = (1, 2, 3)
tuple2 = (1,2,3,1,2,3,4,5,2,3,4,2.4,2)
tuple3 = (2,4,6,6,4,2)
print(remove_fist_value(tuple1,1))
print(remove_fist_value(tuple2,3))
print(remove_fist_value(tuple3,9))