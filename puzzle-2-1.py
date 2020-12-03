class PasswordEntry:
    min_letter = None
    max_letter = None
    letter = None
    password = None

    def isValid(self):
        letterCount = 0
        for letter in self.password:
            if letter == self.letter:
                letterCount += 1
        return letterCount <= self.max_letter and letterCount >= self.min_letter

    def __init__(self, line):
        self.min_letter = int(line[:line.index("-")])
        self.max_letter = int(line[line.index("-") + 1:line.index(" ")])
        self.letter = line[line.index(":") - 1:line.index(":")]
        self.password = line[line.index(":") + 2:]


def getEntries():
    with open('data/data-2.txt') as file:
        return [PasswordEntry(line.rstrip()) for line in file]

# complexity : n * m (n is the number of lines and m is the length of the password)
def getValidPasswords(entries):
    validPasswords = 0
    for entry in entries:
        if entry.isValid():
            validPasswords += 1
    return validPasswords

if __name__ == "__main__":
    print(getValidPasswords(getEntries()))