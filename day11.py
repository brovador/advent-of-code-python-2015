#encoding: utf-8
import sys
import os
import string

def main():
    script_name = os.path.basename(__file__)
    input_file = './{0}-input.txt'.format(os.path.splitext(script_name)[0])

    with open(input_file, 'r') as f:
        commands = [l.strip() for l in f]

    def validate(password):
        valid = True
        if valid:
            valid = valid and all(map(lambda x: x not in password, 'iol'))
        if valid:
            increase = 0
            for i, c in enumerate(password[:-1]):
                increase = increase + 1 if ord(c) + 1 == ord(password[i + 1]) else 0
                if increase == 2:
                    break
            valid = valid and increase == 2
        if valid:
            pairs = 0
            count = 0
            for i, c in enumerate(password[:-1]):
                count = count + 1 if c == password[i + 1] else 1
                pairs = pairs + 1 if count == 2 else pairs
            valid = valid and pairs >= 2
        return valid

    def increment(password):
        invalid_letters = 'iol'
        password = list(password)
        i = 1
        while i < len(password):
            if password[-i] != 'z':
                break
            else:
                i += 1
        l = password[-i]
        if l != 'z':
            nl = chr(ord(l) + 1)
            while nl in invalid_letters:
                nl = chr(ord(nl) + 1)
            password[-i] = nl
            i = i - 1
            while i > 0:
                password[-i] = 'a'
                i = i - 1
        return ''.join(password)

    password = commands[0]
    while True:
        password = increment(password)
        if validate(password):
            break
    print password





if __name__ == '__main__':
    main()
