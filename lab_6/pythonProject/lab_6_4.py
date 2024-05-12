def friend(tuple_some, value):
    if value not in tuple_some:
        return ()
    else:
        for elem in tuple_some:
            if elem == value:
                index = tuple_some.index(value)
                sub_tuple = tuple_some[index:]
                slice_tuple = sub_tuple[1:]
                if value in slice_tuple:
                    index_slice = slice_tuple.index(value)
                    sub_sub = slice_tuple[:index_slice]
                    list1 = [value] + list(sub_sub) + [value]
                    new_tuple = tuple(list1)
                    return new_tuple
                else:
                    return sub_tuple

tuple1 = (1,2,3)
tuple2 = (1,2,8,3,4,8,8,9,2)
tuple3 = (1,2,8,5,1,2,9)

print(friend(tuple1, 8))
print(friend(tuple2, 8))
print(friend(tuple3, 8))
