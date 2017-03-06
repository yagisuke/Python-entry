# 遊園地の入場料の計算プログラム

# 料金
CHILDREN_PRICE = 1000
NORMAL_PRICE = 3000
ELDER_PRICE = 2000

# 入力
children_cnt = int(input("子供料金（13歳未満）は何人ですか？"))
normal_cnt = int(input("通常料金（13から64歳）は何人ですか？"))
elder_cnt = int(input("年配者料金（65歳以上）は何人ですか？"))
total_cnt = children_cnt + normal_cnt + elder_cnt

# 集計
children_price = children_cnt * CHILDREN_PRICE
normal_price = children_cnt * NORMAL_PRICE
elder_price = children_cnt * ELDER_PRICE
total_price = children_price + normal_price + elder_price

# 割引料金の適用
if total_cnt > 10:
    print("団体料金があります。")
    total_price = int(total_price * 0.8)
else:
    print("割引はありません。")

# 結果
print("子供料金: {0}人 x {1}円 = {2}円".format(children_cnt, CHILDREN_PRICE, children_price))
print("通常料金: {0}人 x {1}円 = {2}円".format(normal_cnt, NORMAL_PRICE, normal_price))
print("年配者料金: {0}人 x {1}円 = {2}円".format(elder_cnt, ELDER_PRICE, elder_price))
print("合計: {0}人 {1}円".format(total_cnt, total_price))
