
# 暗号化ライブラリを使ってみる

# 事前作業:
# pip install pycrypto で必要なパッケージをインストールしておく
# mac osxでは、pipコマンドがPython2用のものになっているため、pipをpip3に読み替える
from Crypto.Cipher import AES
import base64


message = "自分がして欲しいと思うことを人にもするように。" # 暗号化したいデータ
password = "password" # 適当なパスワードを指定
iv = "16MOJIhaTEKITOU2" # 初期化ベクトル
mode = AES.MODE_CBC # 暗号化モード

def mkpad(s, size):
    '''特定の長さの倍数にするため空白でデータを埋める関数'''

    s = s.encode("utf-8") # utf-8の文字列をバイト列に変換する
    pad = b' ' * (size - len(s) % size) # 特定の長さの倍数にするための空白を生成
    print('mkpad:', s + pad)
    return s + pad

def encrypt(password, data):
    '''暗号化する'''

    password = mkpad(password, 16) # 16の倍数に揃える
    data = mkpad(data, 16) # バイト列に変換し16の倍数に揃える
    password = password[:16] # 16文字に揃える

    # 暗号化
    aes = AES.new(password, mode, iv)
    data_cipher = aes.encrypt(data)

    return base64.b64encode(data_cipher).decode("utf-8")

def decrypt(password, encdata):
    '''複号化する'''

    password = mkpad(password, 16) # 16の倍数に揃える
    password = password[:16] # バイト列に変換し16の倍数に揃える

    # 複合化
    aes = AES.new(password, mode, iv)
    encdata = base64.b64decode(encdata) # 暗号化データをbase64ででコードしてバイト列に
    data = aes.decrypt(encdata) # 複合化

    return data.decode("utf-8") # 複合化したデータを文字列にする


enc = encrypt(password, message) # 暗号化する
dec = decrypt(password, enc) # 複合化する

# 結果を表示する
print("暗号化:", enc) # 暗号化: 5nhSShwW5Txd6kAuraTSvGhtRSO+W+Dtncsy1TE5nY5T1ssSOaRGeEiD+YAiP8W9EWGlxgq+4WVeX0RBQZvePlFD/8+bGz/Q+ZyOvBev8fM=
print("複合化:", dec) # 複合化: 自分がして欲しいと思うことを人にもするように。
