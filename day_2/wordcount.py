def word_count(phrase):
    ret = {}
    for word in phrase.split():
        if ret.get(word):
            ret[word] += 1
        else:
            ret[word] = 1
    return ret
