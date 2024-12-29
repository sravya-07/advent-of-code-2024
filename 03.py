from aoc_utility import read_input

def get_summ(data):
    summ = 0
    prev = ''
    for i in range(len(data)):
        if data[i] == 'm':
            prev = "m"
        elif data[i] == "u" and prev == "m":
            prev += "u"
        elif data[i] == "l" and prev == "mu":
            prev += "l"
        elif data[i] == "(" and prev == "mul":
            prev += "("
        elif data[i].isdigit() and (prev != '') and (prev == "mul(" or prev[-1].isdigit() or prev[-1] == ','):
            prev += data[i]
        elif (data[i] == ',' or data[i] == ")") and prev != '' and prev[-1].isdigit():
            prev += data[i]
        else:
            prev = ''
        
        if prev != '' and prev[:4] == "mul(" and prev[-1] == ")":
            calc = prev[4:-1].split(',')
            summ += int(calc[0]) * int(calc[1])
    return summ

def get_summ_1(data):
    summ = 0
    prev = ''
    enabled = True
    l = len(data)
    for i in range(l):
        if data[i] == "d":
            if i + 4 <= l and data[i:i+4] == "do()":
                enabled = True
            if i + 7 <= l and data[i:i+7] == "don't()":
                enabled = False

        if data[i] == 'm':
            prev = "m"
        elif data[i] == "u" and prev == "m":
            prev += "u"
        elif data[i] == "l" and prev == "mu":
            prev += "l"
        elif data[i] == "(" and prev == "mul":
            prev += "("
        elif data[i].isdigit() and (prev != '') and (prev == "mul(" or prev[-1].isdigit() or prev[-1] == ','):
            prev += data[i]
        elif (data[i] == ',' or data[i] == ")") and prev != '' and prev[-1].isdigit():
            prev += data[i]
        else:
            prev = ''
        
        if enabled and prev != '' and prev[:4] == "mul(" and prev[-1] == ")":
            calc = prev[4:-1].split(',')
            summ += int(calc[0]) * int(calc[1])
    return summ

if __name__ == "__main__":
    data = read_input(__file__)

    print(get_summ(data))
    print(get_summ_1(data))
