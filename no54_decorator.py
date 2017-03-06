# decorator
# 関数の処理を装飾するための仕組み


def show_func_name(func):
    def wrapper(*args, **kwargs):
        print("--- start: " + func.__name__)
        res = func(*args, **kwargs)
        print("--- end: " + func.__name__)
        return res
    return wrapper

@show_func_name
def kakugen1():
    print("賢い者たちの静かな言葉は")
    print("愚鈍な人々の叫びよりも聞かれる。")

@show_func_name
def kakugen2():
    print("求め続けなさい。そうすれば与えられます。")

kakugen1()
# --- start: kakugen1
# 賢い者たちの静かな言葉は
# 愚鈍な人々の叫びよりも聞かれる。
# --- end: kakugen1
kakugen2()
# --- start: kakugen2
# 求め続けなさい。そうすれば与えられます。
# --- end: kakugen2


import time
import datetime

def time_log(func):
    def wrapper(*args, **kwargs):
        # 前処理
        start = datetime.datetime.today()
        print("--- start", func.__name__)
        # 関数の実行
        result = func(*args, **kwargs)
        # 後処理
        end = datetime.datetime.today()
        delta = end - start
        print("--- end", func.__name__, delta, "sec")
    return wrapper

@time_log
def test1():
    print("sleep 1sec")
    time.sleep(1)

@time_log
def test2():
    print("sleep 2sec")
    time.sleep(2)

test1()
# --- start test1
# sleep 1sec
# --- end test1 0:00:01.003064 sec

test2()
# --- start test2
# sleep 2sec
# --- end test2 0:00:02.003458 sec


def wrap_html(func):
    def wrapper(*args, **kwargs):
        s = "<html>"
        s += func(*args, **kwargs)
        s += "</html>"
        return s
    return wrapper

def wrap_body(func):
    def wrapper(*args, **kwargs):
        s = "<body>"
        s += func(*args, **kwargs)
        s += "</body>"
        return s
    return wrapper

@wrap_html
@wrap_body
def show_html(text):
    return text

print(show_html("<h1>タイトル</h1><p>decoratorトレーニング</p>")) # <html><body><h1>タイトル</h1><p>decoratorトレーニング</p></body></html>
