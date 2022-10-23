def longestChain(words):
    word_dict = {}
    max_chain = 0
    for word in sorted(words, key=len):
        word_dict[word] = 1
        for i in range(len(word)):
            w = word[:i] + word[i+1:]
            if w in words:
                word_dict[word] = max(word_dict[word], word_dict[w]+1)
        max_chain = max(max_chain, word_dict[word])
    return max_chain