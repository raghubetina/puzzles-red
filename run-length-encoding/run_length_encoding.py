from collections import Counter

def decode(string):
    pass


def encode(string):
    listword = []
    for i in string:
        listword.append(i.upper())
    print(Counter(listword))
    print(listword)

encode("AAAAAABBbbcDD")
decode("12AB3CD")