def prob1(file):
    input = open(file, "r").readlines()
    outcomes = {'A X': 4, 'A Y': 8, 'A Z': 3, 
                'B X': 1, 'B Y': 5, 'B Z': 9, 
                'C X': 7, 'C Y': 2, 'C Z': 6}

    score = 0
    for line in input:
        score += outcomes[line.strip()]
    return score

def prob2(file):
    input = open(file, "r").readlines()
    outcomes = {'A X': 3, 'A Y': 4, 'A Z': 8, 
                'B X': 1, 'B Y': 5, 'B Z': 9, 
                'C X': 2, 'C Y': 6, 'C Z': 7}

    score = 0
    for line in input:
        score += outcomes[line.strip()]
    return score