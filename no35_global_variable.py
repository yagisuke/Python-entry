# グローバル変数は関数内から変更できない
global_val = "before"

def cant_cange():
    global_val = "after"
    print(global_val) # after

cant_cange()
print(global_val) # before



# グローバル変数は関数ないからでは変更できない
global_val = "before"

def can_cange():
    global global_val # 関数の外側で共通で利用できるようにするにはglobal宣言する
    global_val = "after"
    print(global_val) # after

can_cange()
print(global_val) # after
