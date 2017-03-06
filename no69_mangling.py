# 非公開メソッド(マングリング: mangling)

class Test:
    def __private_method(self):
        print("非公開メソッド")

    def public_method(self):
        print("公開のメソッド")

test = Test()
test.public_method() # 公開のメソッド
# game.__private_method() AttributeError: 'Game' object has no attribute '__private_method'
test._Game__private_method() # 非公開メソッド
