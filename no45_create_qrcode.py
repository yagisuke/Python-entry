# urlのqrコードを作成する処理

# 事前作業:
# pip install pillow qrcode で必要なパッケージをインストールしておく
# mac osxでは、pipコマンドがPython2用のものになっているため、pipをpip3に読み替える
import qrcode;

# QRコードを生成する
img = qrcode.make("https://github.com/yagisuke")
# QRコードをファイルに保存
img.save("output/no45_qr_yagisuke.png")
