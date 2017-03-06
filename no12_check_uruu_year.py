# うるう年かどうかを確認するプログラム

year = int(input("今年は西暦何年でしたっか？"))

# うるう年の判定
is_uruu_year = False
if (year % 400 == 0):
    is_uruu_year = True
elif (year % 100 == 0):
    is_uruu_year = False
elif (year % 4 == 0):
    is_uruu_year = True
else:
    is_uruu_year = False

# 結果出力
if (is_uruu_year):
    print("あっ！今年はうるう年ですね！")
else:
    print("今年はうるう年じゃないんですね。")
