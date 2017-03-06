#　多重継承（multiple inheritance）

class A:
    def printA(self): print("A")

class B:
    def printB(self): print("B")

class C:
    def printC(self): print("C")

class D(A, B, C): # クラスA, クラスB, クラスCを継承したクラスD
    def printD(self): print("D")

    def printAll(self):
        self.printA()
        self.printB()
        self.printC()
        self.printD()

obj = D() # クラスのインスタンスを作成
obj.printA() # クラスAのprintA()メソッドを実行
obj.printB() # クラスBのprintA()メソッドを実行
obj.printC() # クラスCのprintA()メソッドを実行
obj.printD() # クラスDのprintA()メソッドを実行
obj.printAll() # クラスAllのインスタンスを作成
# A
# B
# C
# D
# A
# B
# C
# D


class A:
    def print_class(self): print("A")

class B:
    def print_class(self): print("B")
    
class C(A, B): # 多重継承時に継承元に同じメソッドがある場合は、左側のクラスが優先される
    pass

obj = C()
obj.print_class() # A
