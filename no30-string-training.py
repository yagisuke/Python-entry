# string操作のトレーニング

# 文字列の繰り返し
go = "GO"
print("マッハ", go * 2) # マッハ GOGO


# 文字列のスライス
love = "LOVE"
print(love[2]) # V
print(love[1::2]) # OE


# 文字列の分割
today = "2017-02-26"
print(today.split("-")) # ['2017', '02', '26']
print(today.split("-", maxsplit = 1)) # ['2017', '02-26']


# 文字列の結合
today = ['2017', '02', '26']
print("/".join(today)) # 2017/02/27


# 文字列の置換
s = "This is a pen."
print(s.replace("pen", "note")) # This is a note.
print(s) # This is a pen.


# 文字列検索(見るからない時は-1を返す)
s = "This is a pen."
print(s.find("h")) # 1
print(s.find("z")) # -1


# 文字列をすべて小文字/大文字に変換する
s = "This is a pen."
print(s.lower()) # this is a pen.
print(s.upper()) # THIS IS A PEN.


# 文字列の始まり、終了の文字列の確認
print(s.startswith("T")) # True
print(s.endswith(".")) # True


# 文字列が数字かどうかを確認する
s = "1234567890"
if s.isnumeric(): print("全部数字です。") # 全部数字です。
