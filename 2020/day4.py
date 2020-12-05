import re

passports = []

with open('inputs/day4','r') as f:
    passport = {}
    for line in f:
        ln = line[:-1] # no \n

        if len(ln)==0:
            passports.append(passport)
            passport = {}
        else:
            x = re.split('([a-z]{3}:)', ln)[1:]
            for k,v in zip(x[::2],x[1:][::2]):
                if k != 'cid:':
                    passport[k] = v.strip()

    ## end of file
    passports.append(passport)

required_fields = sorted(['byr:','iyr:','eyr:','hgt:','hcl:','ecl:','pid:'])


## PART 1
valid = 0
for passport in passports:
    val = sorted(passport.keys()) == required_fields
    valid += 1 if val else 0

print(valid)

### PART 2
def validate(ppt):
    byr = 1920 <= int(ppt['byr:']) <= 2002
    iyr = 2010 <= int(ppt['iyr:']) <= 2020
    eyr = 2020 <= int(ppt['eyr:']) <= 2030
    hgt = ('150cm' <= ppt['hgt:'] <= '193cm') if 'cm' in ppt['hgt:'] else ('59in' <= ppt['hgt:'] <= '76in')
    hcl = True if (re.match('(\#[0-9a-z]{6}$)', ppt['hcl:'])) else False
    ecl = ppt['ecl:'] in ['amb','blu','brn','gry','grn','hzl','oth']
    pid = True if re.match('[0-9]{9}$', ppt['pid:']) else False
    return all([byr,iyr,eyr,hgt,hcl,ecl,pid])


valid = 0
i = 0
for passport in passports:

    if sorted(passport.keys()) == required_fields:
        val = validate(passport)
        valid += 1 if val else 0

        if val:
            s = f""
            for k in required_fields:
                s += (f"{k}{passport[k]} ")

            print(s)
            print()
            i += 1
print(valid)
