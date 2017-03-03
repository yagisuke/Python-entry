
a = 29
b = 29

# 比較式
print(a == b) # True
print(a != b) # False
print(a < b) # False
print(a <= b) # True

# 論理演算子
print(a == b and a < b) # False
print(a != b or a == b) # True
print(not a != b) # True

# 三項演算子
# 変数 = (Trueの値) if (条件) else (Falseの値)
a = 29
print("偶数" if (a % 2 == 0) else "奇数") # 奇数
a = 28
print("偶数" if (a % 2 == 0) else "奇数") # 偶数
