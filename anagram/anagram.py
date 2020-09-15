def find_anagrams(word, candidates):
    sorted_word = ''.join(sorted(word))
    sorted_characters = []

    for word in candidates:
        sorted_char = ''.join(sorted(word))
        if sorted_char == sorted_word:
            sorted_characters.append(word)
    print(sorted_characters)

find_anagrams("enlist", ["inlets", "google", "listen", "grape", "fantastic", "inlet"])
