import re;

# 正規表現のパターンに位置するものを画面に出力
words = ["orange", "october", "octpus", "order", "order", "banana", "baby", "busy"]
pattern = r"^oc.*$"
print("ocで始まるパターン=", pattern)
for word in words:
    if re.match(pattern, word):
        print("=", word)
        # = october
        # = octpus


words = ["orange", "october", "octpus", "order", "order", "banana", "baby", "busy"]
pattern = r"^b.*y$"
print("bで始まりyで終わるパターン", pattern)
for word in words:
    if re.match(pattern, word):
        print("=", word)
        # = baby
        # = busy


words = ["hoge.py", "hoge.img", "hoge.png", "huga.py"]
pattern = r"\.py$"
print("Pythonファイルのパターン", pattern)
for word in words:
    if re.search(pattern, word):
        print("=", word)
        # = hoge.py
        # = huga.py


words = ["Java", "PHP", "Perl", "FLASH", "HTML", "CSS", "Ruby", "Python", "GO", "Swift", "VB.NET", "C#", "C++", "Kotlin"]
pattern = r"^....$"
print("任意の4文字のパターン", pattern)
for word in words:
    if re.search(pattern, word):
        print("=", word)
        # = Java
        # = Perl
        # = HTML
        # = Ruby


word = "青巻紙赤巻紙黄巻紙"
print(re.findall(r".+紙", word)) # ['青巻紙赤巻紙黄巻紙']
print(re.findall(r".+?紙", word)) # ['青巻紙', '赤巻紙', '黄巻紙']


zipre = re.compile(r"^[0-9]{3}\-[0-9]{4}")
print(zipre.search("440-0012")) # <_sre.SRE_Match object; span=(0, 8), match='440-0012'>


word = "i like red color."
pattern = r"\w+ (color|colour)"
print(re.search(pattern, word)) # <_sre.SRE_Match object; span=(7, 16), match='red color'>


word = "date: 2017/10/15"
pattern = r"(\d{4})/(\d{1,2})/(\d{1,2})"
group = re.search(pattern, word)
print(group.groups()) # ('2017', '10', '15')
