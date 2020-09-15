def find_anagrams(word, candidates):
    sorted_word = ''.join(sorted(word)).lower()
    sorted_characters = []

    for word in candidates:
        sorted_char = ''.join(sorted(word)).lower()
        if sorted_char == sorted_word:
            sorted_characters.append(word)

    return sorted_characters

print(find_anagrams("ENLIST", ["inlets", "google", "listen", "grape", "fantastic", "INLETS"]))
