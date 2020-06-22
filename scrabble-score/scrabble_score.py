scores_dict = {
    'aeioulnrst': 1,
    'dg': 2,
    'bcmp': 3,
    'fhvwy': 4,
    'k': 5,
    'jx': 8,
    'qz': 10
}


def score(word: str):
    score_total = 0

    for c in word.lower():
        for key in scores_dict.keys():
            if c in key:
                score_total += scores_dict[key]
                break

    return score_total



print(score('cabbage'))