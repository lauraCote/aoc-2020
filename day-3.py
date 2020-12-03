import functools
import operator

def get_entries():
    with open('data/day-3.txt') as file:
        return [(line.rstrip()) for line in file]

def number_of_trees(entries):
    max_x = len(entries[0])
    return len([1 for index, line in enumerate(entries) if line[((index * 3 + 1) % max_x) - 1] == '#'])

if __name__ == "__main__":
    print(number_of_trees(get_entries()))