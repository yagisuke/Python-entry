# テキストファイルの読み書き

FILENAME = "output/no_47.txt"
UTF8 = "utf-8"

# ファイルの書き込み
# 1, ファイルを開く
# 2, ファイルに書き込み
# 3, ファイルを閉じる
a_file = open(FILENAME, mode="w", encoding=UTF8)
try:
    # ファイルを開いている最中はいつエラーになってもおかしくない(開いたファイルを消されたり..)
    # なので、処理終了時には確実にファイルを閉じるようにする
    a_file.write("私は失敗したことがない\n")
    a_file.write("一万通りの方法を見つけただけだ\n\n")
    a_file.write("トーマス・エジソン\n")
finally:
    a_file.close()


# ファイルの読み込み
# 1, ファイルを開く
# 2, ファイルを読み込む
# 3, ファイルを閉じる
with open(FILENAME, encoding=UTF8) as b_file:
    # 書き込み時と同じく、ファイルを開いている最中はいつエラーになってもおかしくない
    # with構文を使うと自動的にファイルを閉じてくれる
    s = b_file.read()
    print(s)
print("\nーーーーーーーーーー\n")


# ファイルを一行ずつ読み表示
with open(FILENAME, encoding=UTF8) as c_file:

    for i, text in enumerate(c_file):
        print(i + 1, '行目:', text, end="")
        # 1 行目: 私は失敗したことがない
        # 2 行目: 一万通りの方法を見つけただけだ
        # 3 行目:
        # 4 行目: トーマス・エジソン
print("\nーーーーーーーーーー\n")


# キーワードの検索
kw = "た"
with open(FILENAME, encoding=UTF8) as c_file:

    for i, text in enumerate(c_file):
        if text.find(kw) > 0:
            print(i + 1, '行目:', text, end="")
            # 1 行目: 私は失敗したことがない
            # 2 行目: 一万通りの方法を見つけただけだ
