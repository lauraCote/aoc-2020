import functools
import operator

def get_entries():
    with open('data/day-3.txt') as file:
        return [(line.rstrip()) for line in file]

def number_of_trees(entries, right, down):
    max_x = len(entries[0])
    return len([1 for index, line in enumerate(entries) if index % down == 0 and line[(((index // down) * right + 1) % max_x) - 1] == '#'])

def total_trees(entries):
    return number_of_trees(entries, 1, 1) * number_of_trees(entries, 3, 1) * number_of_trees(entries, 5, 1) * number_of_trees(entries, 7, 1) * number_of_trees(entries, 1, 2)

if __name__ == "__main__":
    entries = get_entries()
    print(number_of_trees(entries, 3, 1))
    print(total_trees(entries))