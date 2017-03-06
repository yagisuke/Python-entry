import json;
# json.dumps(obj)    | オブジェクト(obj)をJSON文字列に変換
# json.loads(json)   | JSON文字列をPythonのオブジェクトに変換
# json.dump(obj, fp) | オブジェクト(obj)をJSON形式でファイル(fp)に保存
# json.load(fp)      | JSON形式のファイル(fp)からデータを読み出す

filename = "output/no48_test.json"
data = {
    "no": 5,
    "code": ("jas", 1, 19),
    "scr": "be quick to listen, slow to speak, slow to anger"
}

# jsonの書き込み
with open(filename, "w") as fp:
    json.dump(data, fp) # json形式で表示

# jsonの読み込み
with open(filename, "r") as fp:
    r =json.load(fp)
    print("no=", r["no"]) # no= 5
    print("code=", r["code"]) # code= ['jas', 1, 19]
    print("scr=", r["scr"]) # scr= be quick to listen, slow to speak, slow to anger
