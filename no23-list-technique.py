
# リストの削除1
indexs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
del indexs[3]
print(indexs) # [0, 1, 2, 4, 5, 6, 7, 8, 9]

# リストの削除2
indexs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
del indexs[3:6]
print(indexs) # [0, 1, 2, 6, 7, 8, 9]

# 新たな項目を末尾に追加
indexs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
indexs.append(10)
print(indexs) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 異なるリストを末尾に追加
indexs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
indexs.extend([10, 11, 12, 13])
print(indexs) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# インデックスiの位置に値xを挿入する
indexs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
indexs.insert(3, 33)
print(indexs) # [0, 1, 2, 33, 3, 4, 5, 6, 7, 8, 9]

# リストの中にある値xを削除する　(最初に見つかった要素のみ)
indexs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
indexs.remove(3)
print(indexs) # [0, 1, 2, 4, 5, 6, 7, 8, 9]

# リストの末尾にある要素を取り出し、リストから削除する
indexs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
indexs.pop()
print(indexs) # [0, 1, 2, 3, 4, 5, 6, 7, 8]

# リストの全要素を削除する
indexs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
indexs.clear()
print(indexs) # []

# リストから値を探してその位置を返す
indexs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(indexs.index(3)) # 3

# リストから値を探してその出現回数を返す
indexs = [0, 1, 2, 1, 4, 1, 6, 1, 8, 1]
print(indexs.count(1)) # 5

# リストのソート
indexs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
indexs.sort(reverse=True)
print(indexs) # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# リストの複製(浅いコピー)を返す *深いコピーはcopy.deepcopy()を使用する
indexs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
tmp_indexs = indexs.copy()
print(tmp_indexs) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
