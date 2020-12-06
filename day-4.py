import re

def get_passwords():
    data = open('data/day-4.txt').read().split("\n\n")
    passwords = list(map(lambda password: password.replace('\n', ' ').split(' '), data))
    return list(dict(map(lambda info: info.split(':'), password)) for password in passwords)  

def is_valid(password):
    if not contains_all_fields(password):
        return False

    height_valid = False
    height = re.split(r'(\d+)', password['hgt'])
    if height[2] == 'cm':
        height_valid = 150 <= int(height[1]) <= 193
    if height[2] == 'in':
        height_valid = 59 <= int(height[1]) <= 76 


    hair_valid = len(password['hcl']) == 7 and password['hcl'][:-6] == '#' and re.match(r'[\w-]*$', password['hcl'][-6:]) != None
        
    return all([
        hair_valid,
        height_valid,
        1920 <= int(password['byr']) <= 2002,
        2010 <= int(password['iyr']) <= 2020,
        2020 <= int(password['eyr']) <= 2030,
        re.match(r'^\d{9}$', password['pid']),
        password['ecl'] in { 'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'} 
    ])

def contains_all_fields(password):
    requiredFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    return all(map(lambda info: info in password, requiredFields))

def get_valid_passwords_count(passwords, validator):
    return len([1 for password in passwords if validator(password)])


if __name__ == "__main__":
    passwords = get_passwords()
    print(get_valid_passwords_count(passwords, is_valid))
