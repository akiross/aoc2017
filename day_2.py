from itertools import permutations, starmap

if __name__ == '__main__':
    rows = [[int(x) for x in row.split()] for row in open('input_2.txt')]
    print(sum(max(r) - min(r) for r in rows))
    print(sum([d for d, r in starmap(divmod, permutations(row, 2)) if r == 0][0] for row in rows))
