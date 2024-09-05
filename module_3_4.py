def single_root_words (root_word, *other_words):
    same_words = []
    other_words = list(other_words)
    for i in range(len(other_words)):
        b = other_words[i]
        if root_word.lower() in b.lower():
            same_words.append(other_words[i])
        elif b.lower() in root_word.lower():
            same_words.append(other_words[i])
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)