#encoding: utf-8
import sys

def main(input_file):
    with open(input_file, 'r') as f:
        l = f.readline()
        f = 0
        for i,c in enumerate(l):
            if c == '(':
                f += 1
            else:
                f -= 1
            if f == -1:
                print i + 1
                break


if __name__ == '__main__':
    script, input_file = sys.argv
    main(input_file)
