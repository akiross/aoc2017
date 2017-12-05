with open('./input_5.txt') as fp:
    offsets = [int(r) for r in fp]
    # offsets = [0, 3, 0, 1, -3]
    pc = 0
    count = 0
    while True:
        try:
            old_pc, pc = pc, pc + offsets[pc]
            if offsets[old_pc] >= 3:
                offsets[old_pc] -= 1
            else:
                offsets[old_pc] += 1
            count += 1
        except:
            print('Done in', count, 'steps')
            break
