import string

def count_words(sentence):
    counts = dict()
    words_no_punctuation = sentence.translate(str.maketrans('', '', string.punctuation)).split()
           
    for word in words_no_punctuation:
        word = word.lower()
        if word not in counts:
            counts[word] = 0
        counts[word] += 1

    return counts

print(count_words('\"That\'s the password: \'PASSWORD 123\'!\", cried the Special Agent.\nSo I fled.'))