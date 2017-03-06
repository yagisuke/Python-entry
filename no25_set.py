# 集合型(set)

# setは"重複する値を持たせることはできない"
# setは"順序を持たせることはできない"
color = {"red", "blue", "green", "red"}
print(color) # {'blue', 'red', 'green'}

# 集合の差を求める
box1 = {"ハンマー", "釘", "ペンチ"}
box2 = {"釘", "ペンチ"}
print(box1 - box2) # {'ハンマー'}

# ある要素が集合に含まれているか確認んする方法
skills = {"Java", "Python", "HTML", "CSS", "JS"}
if "Python" in skills:
    print("Python頑張りましょう。")

# 複数の集合をまとめる場合
server_set = {"Java", "Python", "JS"}
front_set = {"HTML", "CSS", "JS"}
skill_set = server_set | front_set
print(skill_set) # {'Python', 'CSS', 'HTML', 'Java', 'JS'}

# 重複する値だけ取得する場合
team_a = {"遠藤", "佐藤", "中村"}
team_b = {"遠藤", "Carlos", "田中"}
kenmu_member = team_a & team_b
print(kenmu_member) # {'遠藤'}
