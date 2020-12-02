def getEntries():
    with open('data/data-1.txt') as file:
        return [int(line.rstrip()) for line in file]

# complexity : n^2
def computeEntries(entries, total):
    entriesSet = set()
    filter(lambda entry: entry < total, entries)
    for entry in entries:
        entriesSet.add(entry)
    for first in entries:
        for second in entries[1:]:
            remaining = total - first - second
            if remaining >= 0 and remaining in entriesSet:
                print("Entries", remaining, second, first)
                return first * second * remaining
    return -1

if __name__ == "__main__":
    print(computeEntries(getEntries(), 2020))