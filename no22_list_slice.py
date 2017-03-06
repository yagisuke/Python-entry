# リストのスライス

indexs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# リスト[ 開始 : 終了 ]
print(indexs[:]) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(indexs[-3:]) # [7, 8, 9]
print(indexs[3:6]) # [3, 4, 5]
print(indexs[:3]) # [0, 1, 2]
print(indexs[0:-3]) # [0, 1, 2, 3, 4, 5, 6]
print(indexs[3:len(indexs)]) # [3, 4, 5, 6, 7, 8, 9]
print(indexs[3:]) # [3, 4, 5, 6, 7, 8, 9]

# リスト[ 開始 : 終了 : ステップ ]
print(indexs[::]) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(indexs[::-1]) # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(indexs[3::]) # [3, 4, 5, 6, 7, 8, 9]
print(indexs[3::1]) # [3, 4, 5, 6, 7, 8, 9]
print(indexs[3::2]) # [3, 5, 7, 9]
