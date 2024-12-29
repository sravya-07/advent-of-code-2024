from aoc_utility import read_input

def safe_report(rep):
    if len(rep) <= 1:
         return True
    trend = rep[1] - rep[0]
    for i in range(1, len(rep)):
        diff = rep[i] - rep[i - 1]
        if abs(diff) >= 1 and abs(diff) <= 3 and diff * trend > 0:
                continue
        else:
            return False
    return True

def can_it_be_safe(rep): # brute force
    subsets = [rep[:i] + rep[i+1:] for i in range(len(rep))]
    for i in subsets:
         if safe_report(i):
              return True
    return False

if __name__ == "__main__":
    data = read_input(__file__, strip=True).split("\n")
    unsafe = 0
    potential_safe = 0 
    for report in data:
        rep = list(map(int, report.split(' ')))
        if not safe_report(rep):
             unsafe += 1
             if can_it_be_safe(rep):
                  potential_safe += 1
    print(len(data) - unsafe)
    print(len(data) - unsafe + potential_safe)