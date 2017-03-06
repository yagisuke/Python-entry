# 牛乳アレルギーの人が食べても大丈夫な料理なのかを確認するプログラム

foodstuff = ["Banana", "Apple", "Fish", "Meat", "Milk"]

for food in foodstuff:

    if food == "Milk":
        print("この料理にはMilkが入っています")
        break

else:
    # 繰り返しのelseブロックは、
    # - 繰り返しを1度も実行しなかった時
    # - breakで繰り返しを抜けなかった時
    print("食べても大丈夫な料理です")
