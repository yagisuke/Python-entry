# tuple

tuple_a = (10, 20, 30)
list_b = [5, 10, 15]

# 参照
first_tuple_a = tuple_a[0]
print("slice tuple:", first_tuple_a) # slice tuple: 10

# slice
slice_tuple_a = tuple_a[1:]
print("slice tuple:", slice_tuple_a) # slice tuple: (20, 30)

# 一度作成したtupleは変更できない
# tuple_a[1] = 0 -> TypeError: 'tuple' object does not support item assignment
# tuple_a.append(40) -> AttributeError: 'tuple' object has no attribute 'append'
# tuple_a.clear() -> AttributeError: 'tuple' object has no attribute 'clear'

# tuple -> list
list_a = list(tuple_a)
print(list_a) # [10, 20, 30]

# list -> tuple
tuple_b = tuple(list_b)
print(tuple_b) # (5, 10, 15)
