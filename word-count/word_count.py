import re

def count_words(sentence):
    counts = dict()
    all_words = sentence.split()
    words_no_punctuation = [re.sub('[^\w\s]', '', w) for w in words];
           
    for i in words_no_punctuation:
        if i in counts:
            counts[i.lower()] += 1
        else:
            counts[i.lower()] = 1

    return counts;

print(count_words('\"That\'s the password: \'PASSWORD 123\'!\", cried the Special Agent.\nSo I fled.'))