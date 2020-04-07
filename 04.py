import re

text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
r_text = re.sub("[.,]", "", text)

heads = [1, 5, 6, 7, 8, 9, 15, 16, 19]

words = r_text.split(" ")

index_dict = {}
for i in range(len(words)):
    if i+1 in heads:
        key = words[i][0]
    else:
        key = words[i][0:2]

    val = text.find(key)
    index_dict[key] = val

print(index_dict)
