# テストの平均点を求めるプログラム


# テストの点数
points = [90, 22, 45, 88, 65]


# for文を使った平均点の求め方
total_point = 0
for point in points:
    total_point = total_point + point

avg_point = total_point / len(points)

print("平均点：", avg_point)


# sumを使った平均点の求め方
avg_point = sum(points) / len(points)

print("平均点：", avg_point)
