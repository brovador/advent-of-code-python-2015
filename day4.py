#encoding: utf-8
import sys
import os
import md5

def main():
    script_name = os.path.basename(__file__)
    input_file = './{0}-input.txt'.format(os.path.splitext(script_name)[0])

    with open(input_file, 'r') as f:
        secret_key = f.read().strip()

    i = 1
    m = md5.new(secret_key + str(i))
    while not m.hexdigest().startswith('000000'):
        i += 1
        m = md5.new(secret_key + str(i))
    print i




if __name__ == '__main__':
    main()
