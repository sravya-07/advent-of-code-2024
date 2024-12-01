from aoc_utility import read_input
import sys
def get_int_list(string):
    return [int(i) for i in string.split(',') if i != '']

def get_distance(list1, list2):
    list1 = get_int_list(list1)
    list2 = get_int_list(list2)
    summ = 0
    for i in range(len(list1)):
        min1 = min(list1)
        min2 = min(list2)
        summ += abs(min1 - min2)
        list1.remove(min1)
        list2.remove(min2)
    return summ

def get_similarity(list1, list2):
    similarity = 0
    list1 = get_int_list(list1)
    list2 = get_int_list(list2)
    for number in list1:
        similarity += (number * list2.count(number))
    
    return similarity

if __name__ == '__main__':
    data = read_input(sys.argv[0], strip=True)

    list1, list2 = '', ''
    lines = data.split('\n')
    for line in lines:
        list1 += line.split('   ')[0] + ','
        list2 += line.split('   ')[1] + ','
    
    print('distance:', get_distance(list1, list2))
    print('similarity:', get_similarity(list1, list2))
