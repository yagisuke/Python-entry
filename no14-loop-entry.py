# ループ処理

# for文
for i in range(3):
    print("ループ回数:", i)

# for文: 1から10の和を求める
v = 0
for i in range(1, 11):
    v += i
    print("vに", i, "を足しました" )
print("1から10の合計は", v)

# while文
energy = 3
while energy > 0:
    print("+ 走る | energy=", energy)
    energy -= 1; # 変数の値を1つ増やす

energy = 3
while 6 > energy:
    print("+ 走る | energy=", energy)
    energy += 1; # 変数の値を1つ減らす


# 坪から平方メートルを求めるプログラム
# break
while True:
    # 入力処理
    user = input("あなたのお家の坪数はいくつ？")
    # 終了条件
    if user == "" or user == "q": break
    # 処理結果
    tsubo = int(user)
    m2 = tsubo * 3.31
    print("{0}坪は {1}平方メートルです。".format(tsubo, m2))
