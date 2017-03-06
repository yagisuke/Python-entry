# 辞書型の使い方

# 変数 = {"Key1": Key値1, "Key2": Key値2, "Key3": Key値3}
member_age = {"鈴木": 30, "井上": 20, "伊藤": 22}
print(member_age) # {'鈴木': 30, '井上': 20, '伊藤': 22}


# 辞書型のデータ設定と参照
member_age["井上"] = 23
print(member_age["井上"]) # 23
print(member_age) # {'鈴木': 30, '井上': 23, '伊藤': 22}


# 辞書型にキーが含まれているか
print("井上" in member_age) # True
print("たけし" in member_age) # False


# keyの列挙
print(member_age.keys()) # dict_keys(['鈴木', '井上', '伊藤'])


# keyの列挙をリストに変換
print(list(member_age.keys())) # ['鈴木', '井上', '伊藤']


# key順にソートしてリストを作成
dict_program_rank = {"2": "Python", "5": "GO", "4": "PHP", "3": "Ruby", "1": "Java"}
sorted_keys = sorted(list(dict_program_rank.keys()))

program_rank = []
for key in sorted_keys:
    program_rank.append(dict_program_rank[key])

print(program_rank) # ['Java', 'Python', 'Ruby', 'PHP', 'GO']


# keyと値を一気に取得
cart_items = {"ばなな": 150, "納豆": 99, "りんご": 388}

for name, price in cart_items.items():
    print("{0}の料金は{1}円です。".format(name, price))
    # ばななの料金は150円です。
    # 納豆の料金は99円です。
    # りんごの料金は388円です。
