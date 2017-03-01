import datetime;


# 今日日付の取得
print(datetime.date.today()) # 2017-03-02


# 現在時刻の取得
t = datetime.datetime.now()
print(t.strftime("%Y/%m/%d %H:%M:%S")) # 2017/03/02 00:02:14


# 日付を代入
print(datetime.date(2016, 9, 8)) # 2016-09-08


# 日付の計算
t = datetime.date(2017, 4, 20)
print(t + datetime.timedelta(weeks=1)) # 2017-04-27
print(t - datetime.timedelta(days=3)) # 2017-04-17


# 日付の差
a = datetime.date(2017, 3, 3)
b = datetime.date(2018, 3, 3)
c = b - a
print(c) # 365 days, 0:00:00


# 2020年東京オリンピックの日付
t1 = datetime.date(2020, 7, 24)
t2 = datetime.date.today()
diff = t1 -t2
print("今日:", t2.strftime("%Y/%m/%d")) # 今日: 2017/03/02
print("あと", diff.days, "日") # あと 1240 日
