# for構文と同じ機能の関数を作ってみる

def for_func(iterable, callback):
    '''for構文と同じ機能'''

    it = iter(iterable)
    while True:
        try:
            v = next(it)
            callback(v)
        except StopIteration:
            break

# リストの内容をすべて画面に出力
nums = [1, 2, 3]
for_func(
    nums,
    lambda i : print(i))

# 辞書型の内容をすべて画面に出力
ages = {"Taro": 20, "Jiro": 15, "Saburo": 18}
for_func(
    ages.items(),
    lambda n : print(n))
