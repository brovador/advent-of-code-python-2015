#encoding: utf-8
import sys
import os
import re

def main():
    script_name = os.path.basename(__file__)
    input_file = './{0}-input.txt'.format(os.path.splitext(script_name)[0])

    with open(input_file, 'r') as f:
        commands = [l.strip() for l in f]

    r = re.compile(r'\\x(\w\w)')
    n_chars = 0
    memory_size = 0
    for c in commands:

        ## Decode
        # n_chars += len(c)
        # c = c[1:-1].decode('string_escape')
        # memory_size += len(c)

        def encode_chr(x):
            if x == '"':
                return r'\"'
            elif x == '\\':
                return r'\\'
            else:
                return x

        n_chars += len(c)
        c = ''.join(map(encode_chr, c))
        memory_size += len(c) + 2

    print memory_size - n_chars


if __name__ == '__main__':
    main()
