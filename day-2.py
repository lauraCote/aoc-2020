import re

class PasswordEntry:
    regex = re.compile(r"(\d+)-(\d+) ([a-z]+): ([a-z]+)")
    first_policy: int
    second_policy: int
    letter: str
    password: str

    def is_valid_part_one(self):
        letter_count = self.password.count(self.letter)
        return self.first_policy <= letter_count <= self.second_policy

    def is_valid_part_two(self):
        indexes = self.letter_indexes()
        first_policy_valid = self.first_policy in indexes
        second_policy_valid = self.second_policy in indexes
        return (first_policy_valid and not second_policy_valid) or (not first_policy_valid and second_policy_valid)

    def letter_indexes(self):
        return [pos + 1 for pos, char in enumerate(self.password) if char == self.letter]

    def __init__(self, line):
        first, second, self.letter, self.password = self.regex.match(line).groups("ALL")
        self.first_policy = int(first)
        self.second_policy = int(second)


def get_entries():
    with open('data/day-2.txt') as file:
        return [PasswordEntry(line.rstrip()) for line in file]

# complexity : n * m (n is the number of lines and m is the length of the password)
def get_valid_passwords_part_one(entries):
    return len(list(filter(lambda entry: entry.is_valid_part_one(), entries)))

def get_valid_passwords_part_two(entries):
    return len(list(filter(lambda entry: entry.is_valid_part_two(), entries)))

if __name__ == "__main__":
    entries = get_entries()
    print(get_valid_passwords_part_one(entries))
    print(get_valid_passwords_part_two(entries))