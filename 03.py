import re

text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
r_text = re.sub("[.,]", "", text)

words = r_text.split(" ")

for word in words:
    print(len(word))

