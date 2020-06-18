def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('String should be same length.')

    return sum(i != k for i, k in zip(strand_a, strand_b))
