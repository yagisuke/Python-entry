# ユーザから入力を得る方法

# INPUTさん、おはようございます！
name = input("お名前はなんですか？")
print(name + "さん、おはようございます！")

# INPUTinch = 2.54cm
per_inch = 2.54
inch = float(input("inch?"))
cm = inch * per_inch
print("{0}inch = {1}cm".format(inch, cm))

# INPUTカラット = 4.4グラム
per_ct = 0.2
user = input("なんカラットだった？")
ct = float(user)
g = ct * per_ct
desc = "{0}カラット = {1}グラム".format(ct, g)
print(desc)

# 給料計算
user = input("あなたの時給はいくらですか？")
jikyu = int(user);

user = input("何時間働きましたか？")
jikan = int(user)

kyuryou = jikyu * jikan
fmt = """
時給{0}円のあなたが、{1}時間働いたってことは、
{2}円振り込まれるってことですね！
ごちそうさまです。
"""
print(fmt.format(jikyu, jikan, kyuryou))
