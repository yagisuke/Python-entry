# sorted(iterable[, key][, reverse])

# tupleをソートする
animal_list = [
    ("ライオン", 58),
    ("チーター", 110),
    ("シマウマ", 60),
    ("トナカイ", 80)
]

faster_list = sorted(
    animal_list,
    key = lambda ani : ani[1],
    reverse = True)

for i in faster_list: print(i)


# dictをソートする
animal_dict = {
    "ライオン": 58,
    "チーター": 110,
    "シマウマ": 60,
    "トナカイ": 80
}
li = sorted(
    animal_dict.items(),
    key = lambda x: x[1],
    reverse = True)
print(li)
for name, speed in li:
    print(name, speed)
