def abbreviate(words):
    return ''.join([
        c[0] for c in words.upper().replace('-', ' ').translate(str.maketrans('', '', '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~')).split()
    ])
