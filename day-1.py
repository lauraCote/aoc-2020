def getEntries():
    with open('data/day-1.txt') as file:
        return [int(line.rstrip()) for line in file]

# complexity : nlogn
def computeEntriesPartOne(entries, total):
    entries.sort()
    entries = list(filter(lambda entry: entry < total, entries))
    for entry in entries:
        found = findEntry(entries, 0, len(entries) - 1, total - entry)
        if found != -1:
            return entries[found] * entry


def findEntry(entries, lowerbound, upperbound, entry): 
    if upperbound >= lowerbound: 
        middle = (upperbound + lowerbound) // 2
        if entries[middle] == entry: 
            return middle 
        if entries[middle] > entry: 
            return findEntry(entries, lowerbound, middle - 1, entry) 
    
        return findEntry(entries, middle + 1, upperbound, entry)
    return -1

def computeEntriesPartTwo(entries, total):
    entriesSet = set()
    entries = list(filter(lambda entry: entry < total, entries))
    for entry in entries:
        entriesSet.add(entry)
    for first in entries:
        for second in entries[1:]:
            remaining = total - first - second
            if remaining >= 0 and remaining in entriesSet:
                return first * second * remaining
    return -1

if __name__ == "__main__":
    print(computeEntriesPartOne(getEntries(), 2020))
    print(computeEntriesPartTwo(getEntries(), 2020))