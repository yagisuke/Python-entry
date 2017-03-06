# メソッドのオーバーライド

class SuperClass:

    def hoge(self, id):
        print("---")
        print("SuperClass.hoge=", id)

class SubClass(SuperClass):

    def hoge(self, id): # SuperClassのメソッドと同名のメソッドを定義
        super().hoge(id)
        print("SubClass.hoge=", id)

id1 = SuperClass()
id1.hoge(5)
# ---
# SuperClass.hoge= 5

id2 = SubClass()
id2.hoge(10)
# ---
# SuperClass.hoge= 10
# SubClass.hoge= 10
