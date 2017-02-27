# 関数トレーニング

# 再帰関数
def say_hello(i):
    if i <= 0:
        return
    print("ハロー", i) # ハロー i
    say_hello(i - 1)

say_hello(10)


# 再帰関数
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

print(fact(3)) # 6
print(fact(5)) # 120


# 引数の初期値を指定する
def convert_jou(jou, unit="江戸間"):
    if unit == "江戸間":
        base = 0.88 * 1.76
    elif unit == "京間":
        base = 0.955 * 1.91
    elif unit == "中京間":
        base = 0.91 * 1.82
    m2 = jou * base
    s = "{0}で{1}畳は{2}㎡".format(unit, jou, m2)
    print(s)

convert_jou(6, "江戸間") # 江戸間で6畳は9.2928㎡
convert_jou(6, "京間") # 京間で6畳は10.9443㎡
convert_jou(6) # 江戸間で6畳は9.2928㎡


# 名前付き引数の指定
# - 関数を呼び出す時に、値の意味を明示できる
# - プログラムの書き間違えを減らせる
def calcTime(dist, speed):
    t = dist / speed
    t = round(t, 1)
    return t

print(calcTime(500, 100))
print(calcTime(dist = 500, speed = 100))


# 可変長引数を指定するときに、*変数を指定するとタプルに
def sumArgs(*args): # 変数argsにtupleとして代入されている
    v = 0
    for n in args:
        v += n
    return v

print(sumArgs(1, 2, 3)) # 6


# 可変長引数を指定するときに、"**変数"を指定すると辞書型に
def print_args(**args):
    print(args)

print_args(a = 30, b = 50, c = 40) # {'a': 30, 'b': 50, 'c': 40}
print_args(aa = "hoge", bb = "huga") # {'aa': 'hoge', 'bb': 'huga'}
