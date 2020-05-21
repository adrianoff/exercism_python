def two_fer(name=None):
    return "One for %s, one for me." % (str(name) if name is not None else 'you')
