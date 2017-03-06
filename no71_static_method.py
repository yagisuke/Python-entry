# staticメソッド

class Hoge:
    @staticmethod
    def introduce():
        print("Hoge")

# インスタンスを作る必要がない
# メソッドに引数selfを指定する必要がない
Hoge.introduce() # Hoge
