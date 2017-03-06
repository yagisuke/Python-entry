# 正規表現

import re;

# patternがstrの先頭にマッチするか調べてmatchオブジェクトを返す
pattern = r"This"
str = "This pen is 100yen."

print("re.match", re.match(pattern, str)) # re.match <_sre.SRE_Match object; span=(0, 4), match='This'>


# strのどこかにpatternにマッチするものがあるのか調べてオブジェクトを返す
pattern = r"pen"
str = "This pen is 100yen."

print("re.search", re.search(pattern, str)) # re.search <_sre.SRE_Match object; span=(5, 8), match='pen'>


# patternでstrを分割してリストで返す
pattern = r" is "
str = "This pen is 100yen."

print("re.split", re.split(pattern, str)) # re.split ['This pen', '100yen.']


# strの中でpatternにマッチするものをすべて操作し、文字列のリストとして返す
pattern = r"100"
str = "This pen is 100yen."

print("re.findall", re.findall(pattern, str)) # re.findall ['100']


# strの中でpatternにマッチするものを探すイテレータとして返す
pattern = r"en"
str = "This pen is 100yen."

print("re.finditer", re.finditer(pattern, str)) # re.finditer <callable_iterator object at 0x1014a47b8>


# strの中でpatternにマッチするものをreplに置換する
pattern = r"100"
str = "This pen is 100yen."
repl = r"150"
print("re.sub", re.sub(pattern, repl, str)) # re.sub This pen is 150yen.


# patternをあらかじめコンパイル
pattern = r"\s\w\w\w\s"

print("re.compile", re.compile(pattern)) # re.compile re.compile('\\s\\w\\w\\w\\s')
