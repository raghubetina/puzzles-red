def find_anagrams(word, candidates):
    anagram_list = []
    for i in word: 
        for j in candidates: 
            if i != j and (sorted(i)==sorted(j)):
                anagram_list.append(j)
    return (anagram_list)

    #word_list = list(word)
    #word_list.sort()
    #candidates_list = list(candidates)
    #candidates_list.sort()

    #return (word_list == candidates_list)

word = ["listen"]
candidates = ["enlists", "google", "inlets", "banana"]

#print(word)
#print(candidates)
print(find_anagrams(word, candidates))