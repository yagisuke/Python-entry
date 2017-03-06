# generator
# generatorとは独自のiteratorを作成する仕組み
def gen1to3():
    yield 1; # generatordではreturn文ではなく、yield文を使う
    yield 2;
    yield 3;

it = gen1to3() # イテレータオブジェクトを取得
print(next(it))
print(next(it))
print(next(it))
# print(next(it)) ERROR: StopIteration

print("ーーーー")


# 奇数を返却するiterator
def genOdd(bigin_num=1, max_num=30):
    '''奇数のみ返却するイテレータ'''

    i = bigin_num
    while i <= max_num:
        if i % 2 != 0: yield i
        i += 1

it = genOdd(bigin_num=5, max_num=10)
for i in it:
    print(i, end=",") # 5,7,9,

print("\r\nーーーー")


# 素数を返却するiterator
def genPrime(max_num = 15):
    num = 2
    while (num <= max_num):
        is_prime = True
        for i in range(2, num):
            if (num % i) == 0:
                is_prime = False
                break
        if (is_prime):
            yield num
        num += 1

it = genPrime(50)
for i in it:
    print(i, end=",") # 2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,
