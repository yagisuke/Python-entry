# ランダムモジュールを使ってみる
import random;


# サイコロ
print("サイコロは", random.randint(1, 6), "が出ました。")


# じゃんけん
hands = ["グー", "チョキ", "パー", "ゲーム終了"]

print("\r\n============== じゃんけんしましょう ==============\r\n")

while True:

    com = random.randint(0, 2)

    for i, desc in enumerate(hands):
        print(i, ":", desc)

    you = int(input("出す手を数値で入力してください。"))
    if you == 3: break
    if you <0 or you> 2:
        print("0から3の間で入力してね")
        continue

    print("\r\nーーー\r\n")
    print("自分:", hands[you])
    print("相手:", hands[com])
    print("\r\nーーー\r\n")

    j = (you - com + 3) % 3
    if j == 0:
        print("あいこ")
    elif j == i:
        print("まけちゃったー")
    else:
        print("かったねー！おめでとう♪")

    print("\r\nーーー\r\n")
