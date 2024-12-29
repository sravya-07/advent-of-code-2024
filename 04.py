from aoc_utility import read_input

def get_count(array, word):
    print(*array, sep="\n")
    print('...')
    count = 0
    for item in array:
        if word in item:
            print(item, word)
            count += item.count(word)
        if word[::-1] in item:
            print(item, word[::-1])
            count += item.count(word[::-1])
    print('..')
    return count

def part1(data):
    count = 0
    lines = data.strip().split("\n")

    transverse = []
    for j in range(len(lines[0])):
        item = ''
        for i in range(len(lines)):
            item += lines[i][j]
        transverse.append(item)
    
    rows, cols = len(lines), len(lines[0])
    diagonals1 = []
    count1 = 0
    for k in range(len(lines)):
        r, c = k, 0
        item = ""
        while r < rows and c < cols:
            item += lines[r][c]
            r += 1
            c += 1
        if 'XMAS' in item:
            count1 += 1
        if 'SAMX' in item:
            count1 += 1
        diagonals1.append(item)
    
    for k in range(1, cols):
        item = ""
        r, c = 0, k
        while r < rows and c < cols:
            item += lines[r][c]
            r += 1
            c += 1
        if 'XMAS' in item:
            count1 += 1
        if 'SAMX' in item:
            count1 += 1
        diagonals1.append(item)
    
    diagonals2 = []
    count2 = 0
    for k in range(rows):
        item = ''
        r, c = 0, cols-1-k
        while r < rows and c >= 0:
            item += lines[r][c]
            r += 1
            c -= 1
        if 'XMAS' in item:
            count2 += 1
        if 'SAMX' in item:
            count2 += 1
        diagonals2.append(item)

    for k in range(cols-2, -1, -1):
        item = ""
        r, c = rows-1, k
        while r >= 0 and c >= 0:
            item += lines[r][c]
            r -= 1
            c -= 1
        if 'XMAS' in item:
            count2 += 1
        if 'SAMX' in item:
            count2 += 1
        diagonals2.append(item)
    
    return get_count(lines, 'XMAS') + get_count(transverse, 'XMAS') + count1 + count2
# get_count(diagonals1, 'XMAS') + get_count(diagonals2, 'XMAS')


if __name__ == "__main__":
    data = read_input(__file__)
    print(part1(data))