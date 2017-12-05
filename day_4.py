from collections import Counter

with open('./input_4.txt') as fp:
    num, add = 0, 0
    for line in fp:
        num += Counter(line.split()).most_common(1)[0][1] == 1
        add += Counter(''.join(sorted(w)) for w in line.split()).most_common(1)[0][1] == 1
    print(num, add)

