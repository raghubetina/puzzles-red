def count_words(sentence):
    counts = dict()
    words = sentence.split()

    for i in words:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1

    return counts;

print(count_words('\"That\'s the password: \'PASSWORD 123\'!\", cried the Special Agent.\nSo I fled.'))