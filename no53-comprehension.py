# リスト内包表記

# リスト内包表記をしない場合
data = []
for i in range(1, 6):
    data.append(i * 2)
print(data) # [2, 4, 6, 8, 10]


# リスト内包表記をする場合
data = [i for i in range(1, 6)]
print(data) # [1, 2, 3, 4, 5]


data = [i * 2 for i in range(1, 6)]
print(data) # [2, 4, 6, 8, 10]


data = [(i * 2 - 1) for i in range(1, 6)]
print(data) # [1, 3, 5, 7, 9]


data = list(map(lambda x : x * 2, range(1, 6)))
print(data) # [2, 4, 6, 8, 10]


data = [i for i in range(1, 6) if i % 2 == 1]
print(data) # [1, 3, 5]


result = []
base = [1, 2, 3]
for x in base:
    for y in base:
        result.append((x, y))
print(result) # [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]


base = [1, 2, 3]
result = [(x, y) for x in base for y in base if x != y]
print(result) # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]


res = [
    "Fizz Buzz" if i % 15 == 0 else "Fizz"
                if i % 3 == 0 else "Buzz"
                if i % 5 == 0 else str(i)
    for i in range(1, 17)
]
print("\n".join(res))
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# Fizz Buzz
# 16


print([x**2 for x in [1, 2, 3]]) # [1, 4, 9]


print({(x + y) for x in [1,2,3] for y in [1, 2, 3]}) # {2, 3, 4, 5, 6}


print([(x + y) for x in [1,2,3] for y in [1, 2, 3]]) # [2, 3, 4, 3, 4, 5, 4, 5, 6]


print({"h" + str(x) : x*5 for x in range(1, 4)}) # {'h1': 5, 'h2': 10, 'h3': 15}


gen = (x ** 2 for x in [1, 2, 3])
for i in gen:
    print(i)
    # 1
    # 4
    # 9
