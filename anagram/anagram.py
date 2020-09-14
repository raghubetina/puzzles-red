def find_anagrams(word, candidates):
    anagram_list = []
    for i in word: 
        for j in candidates: 
            if i != j and (sorted(i)==sorted(j)):
                anagram_list.append(j)
    return (anagram_list)

word = ["listen"]
candidates = ["enlists", "google", "inlets", "banana"]

print(find_anagrams(word, candidates))