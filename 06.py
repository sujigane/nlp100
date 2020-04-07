import sys

def n_gram(n, text):
    n_gram_list = []
    for i in range(len(text)-n+1):
        n_gram_list.append(text[i:i+n])

    return n_gram_list

if __name__ == "__main__":
    x_str = "paraparaparadise"
    y_str = "paragraph"

    x_bigram = n_gram(2, x_str)
    y_bigram = n_gram(2, y_str)

    union = set(x_bigram) | set(y_bigram)
    intsect = set(x_bigram) & set(y_bigram)
    diff = set(x_bigram) - set(y_bigram)

    print("X: {}".format(x_bigram))
    print("Y: {}".format(y_bigram))

    print("和集合: {}".format(union))
    print("積集合: {}".format(intsect))
    print("差集合: {}".format(diff))

    if "se" in x_bigram:
        print("'se'はXに含まれる")
    else:
        print("'se'はXに含まれない")

    if "se" in y_bigram:
        print("'se'はYに含まれる")
    else:
        print("'se'はYに含まれない")

