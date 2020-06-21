from collections import Counter


def count_words(sentence):
    words = list(map(
        lambda s: s.strip("'"),
        sentence.
            replace(',', ' ').
            replace('_', ' ').
            translate(str.maketrans('', '', '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~')).
            lower().
            split()
    ))

    # words_count = {}
    # for word in words:
    #     words_count[word] = words_count.setdefault(word, 0) + 1

    return Counter(words)
