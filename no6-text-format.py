# formatで値を埋め込む方法
name = "Carlos"
age = "28"
str = "{0}は{1}歳になりました.".format(name, age)
print(str) # Carlosは28歳になりました。

# formatで名前付き引数を使う方法
print("私は{sports_name}が好きです.".format(sports_name="Soccer")) # 私はSoccerが好きです
format = "私は{pet}を飼っています."
print(format.format(pet="Dog")) # 私はDogを飼っています
