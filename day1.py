#encoding: utf-8
import os

def main():

    script_name = os.path.basename(__file__)
    input_file = './{0}-input.txt'.format(os.path.splitext(script_name)[0])

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
    main()
