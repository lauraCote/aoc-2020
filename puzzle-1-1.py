def getEntries():
    with open('data/data-1.txt') as file:
        return [int(line.rstrip()) for line in file]

# complexity : nlogn
def computeEntries(entries, total):
    entries.sort()
    filter(lambda entry: entry < total, entries)
    for entry in entries:
        if entry >= total:
            return -1
        found = findEntry(entries, 0, len(entries) - 1, total - entry)
        if found != -1:
            return entries[found] * entry
    return -1

def findEntry(entries, lowerbound, upperbound, entry): 
    if upperbound >= lowerbound: 
        middle = (upperbound + lowerbound) // 2
        if entries[middle] == entry: 
            return middle 
        if entries[middle] > entry: 
            return findEntry(entries, lowerbound, middle - 1, entry) 
    
        return findEntry(entries, middle + 1, upperbound, entry)
    return -1

if __name__ == "__main__":
    print(computeEntries(getEntries(), 2020))