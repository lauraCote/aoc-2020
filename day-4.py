import re

def get_passports():
    data = open('data/day-4.txt').read().split("\n\n")
    passports = list(map(lambda passport: passport.replace('\n', ' ').split(' '), data))
    return list(dict(map(lambda info: info.split(':'), passport)) for passport in passports)  

def is_valid(passport):
    if not contains_all_fields(passport):
        return False

    height_valid = False
    height = re.split(r'(\d+)', passport['hgt'])
    if height[2] == 'cm':
        height_valid = 150 <= int(height[1]) <= 193
    if height[2] == 'in':
        height_valid = 59 <= int(height[1]) <= 76 

    hair_valid = len(passport['hcl']) == 7 and passport['hcl'][:-6] == '#' and re.match(r'[\w-]*$', passport['hcl'][-6:]) != None
        
    return all([
        hair_valid,
        height_valid,
        1920 <= int(passport['byr']) <= 2002,
        2010 <= int(passport['iyr']) <= 2020,
        2020 <= int(passport['eyr']) <= 2030,
        re.match(r'^\d{9}$', passport['pid']),
        passport['ecl'] in { 'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'} 
    ])

def contains_all_fields(passport):
    requiredFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    return all(map(lambda info: info in passport, requiredFields))

def get_valid_passports_count(passports, validator):
    return len([1 for passport in passports if validator(passport)])


if __name__ == "__main__":
    passports = get_passports()
    print(get_valid_passports_count(passports, contains_all_fields))
    print(get_valid_passports_count(passports, is_valid))
