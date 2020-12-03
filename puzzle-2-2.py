class PasswordEntry:
    firstIndex = None
    secondIndex = None
    letter = None
    password = None

    def isValid(self):
        hasSeenLetter = False
        for index, letter in enumerate(self.password):
            if letter == self.letter:
                if index + 1 == self.firstIndex or index + 1 == self.secondIndex:
                    if hasSeenLetter:
                        return False
                    hasSeenLetter = True
        return hasSeenLetter

    def __init__(self, line):
        self.firstIndex = int(line[:line.index("-")])
        self.secondIndex = int(line[line.index("-") + 1:line.index(" ")])
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