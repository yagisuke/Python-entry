# 今日は肉の日？

input_day = int(input("今日の日付を入力してね。"))
oniku_day = 29
is_oniku_day = False

if (input_day != oniku_day):
    # 何もしない場合はpassする。
    pass
else:
    is_oniku_day = True

# 結果の出力＜単文のIF文＞
if (is_oniku_day):
    print("お肉の日ですよ！")
else:
    print("お肉ばかり食べてないで野菜も食べなさい。")
