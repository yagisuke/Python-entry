# iterator
# iteratorとは値を1つずつ順に取り出すための仕組み

# range()関数
for i in range(1, 4):
    print(i)

print("ーーーー")


# リストを使う場合
nums = [1, 3, 6, 9]
for i in nums:
    print(i)

print("ーーーー")


# リストからiteratorを取り出す場合
nums = [1, 3, 6]
print(iter(nums)) # <list_iterator object at 0x1007fa3c8>

i = iter(nums)
print(next(i)) # 1
print(next(i)) # 3
print(next(i)) # 6
# print(next(i)) ERROR: StopIteration

print("ーーーー")


# range()関数のiteratorを取り出す場合
i = iter(range(1, 4))
print(next(i)) # 1
print(next(i)) # 2
print(next(i)) # 3
# print(next(i)) ERROR: StopIteration

print("ーーーー")
