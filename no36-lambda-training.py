# 無名関数(lambda)トレーニング

# lambda 引数1, 引数2: 式
tri = lambda a, b : a * b / 2
print(tri(13, 15)) # 97.5

# 関数の引数に無名関数を指定する
def calc_5_3(func):
    return func(5, 3)

result = calc_5_3(lambda a, b: a * b)
print(result) # 15

result = calc_5_3(lambda a, b: a + b)
print(result) # 8
