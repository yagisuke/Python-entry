# 本の印税を計算する関数

# 印税を計算する関数
def calc_royalty(price, sales, per):
    rate = per / 100
    ro = int(price * sales * rate) # 印税 = 定価 x 発行部数 x 印税率
    return ro

# INPUT
i = input("定価はいくらですか？")
price = int(i)

i = input("発行部数はどのくらいですか？")
sales = int(i)

i = input("印税率(パーセント)はどのくらいですか？")
per = float(i)

v = calc_royalty(price, sales, per)
print("印税は、", v, "円です")
