# テストの赤点の人数を確認するプログラム

# テストの点数
classA_points = [88, 32, 47, 24, 64]
classB_points = [28, 52, 66, 4, 21]
classC_points = [76, 32, 0, 54, 94]

# +でリストを結合
classAll_points = classA_points + classB_points + classC_points

# +=でリストを結合
# classAll_points = []
# classAll_points += classA_points
# classAll_points += classB_points
# classAll_points += classC_points

# extendでリストを結合
# classAll_points = []
# classAll_points.extend(classA_points)
# classAll_points.extend(classB_points)
# classAll_points.extend(classC_points)

# 各クラスの合計点 / 平均点
total_classAll_points = sum(classAll_points)
avg_classAll_points = total_classAll_points / len(classAll_points)

# 赤点を取得
akaten_point = int(avg_classAll_points) / 2
akatens = []
for point in classAll_points:
    if point <= akaten_point:
        akatens.append(point)

print("赤点対象者は合計", len(akatens), "人です。")
