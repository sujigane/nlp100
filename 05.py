import sys

def n_gram(n, text):
    n_gram_list = []
    for i in range(len(text)-n+1):
        n_gram_list.append(text[i:i+n])

    return n_gram_list

if __name__ == "__main__":
    text = "I am an NLPer"
    words = text.split(" ")

    print(text)
    print("　単語bi-gram: {}".format(n_gram(2, words)))
    print("　文字bi-gram: {}".format(n_gram(2, text)))
