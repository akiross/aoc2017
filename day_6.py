def redistribute(banks):
    # Find largest
    l = 0
    for i, v in enumerate(banks):
        if v > banks[l]:
            l = i
    # Redistribute
    c = banks[l]
    banks = list(banks)
    banks[l] = 0
    for i in range(c):
        banks[(l+i+1)%len(banks)] += 1
    return tuple(banks)

def stepper(banks):
    found = set()
    count = 0
    while banks not in found:
        found.add(banks)
        # Redistribute
        banks = redistribute(banks)
        # Count
        count += 1
    return count, banks

banks = (0, 2, 7, 0)
banks = tuple(int(n) for n in open('./input_6.txt').read().split())
c1, banks = stepper(banks)
c2, _ = stepper(banks)
print('Count', c1, c2)
