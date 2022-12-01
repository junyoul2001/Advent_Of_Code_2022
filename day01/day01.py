def prob1(file):
    input = open(file, "r").readlines()

    max = 0
    curr_max = 0
    for line in input:
        if line.strip() == "":
            if curr_max > max:
                max = curr_max
            curr_max = 0
        else:
            curr_max += int(line.strip())

    return max

def prob2(file):
    input = open(file, "r").readlines()

    max = [0, 0, 0]
    curr_max = 0
    for line in input:
        if line.strip() == "":
            for i in range(len(max)):
                if curr_max > max[i]:
                    max[i] = curr_max
                    break
            max = sorted(max)
            curr_max = 0
        else:
            curr_max += int(line.strip())

    return sum(max)