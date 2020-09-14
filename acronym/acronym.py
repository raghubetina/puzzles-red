def abbreviate(words):
    i = 0
    acronym = ""
    while i <= len(words)-1: 
        letter = words[i]
        if i == 0: 
            acronym = acronym + letter.upper()
            i = i + 1
        if words[i-1] == " ": 
            acronym = acronym + letter.upper()
            i = i + 1
        i = i+1
    print(acronym)