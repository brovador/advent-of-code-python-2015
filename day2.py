#encoding: utf-8
import sys

def main(input_file):

    lines = []
    with open(input_file, 'r') as f:
        lines = [[int(x) for x in l.strip().split('x')] for l in f]

    wrap = 0
    ribbon = 0
    for l, w, h in lines:
        a1 = l * w
        a2 = w * h
        a3 = h * l

        wrap += 2 * (a1 + a2 + a3)
        wrap += min([a1, a2, a3])

        mins = [l, w, h]
        mins.remove(max([l, w, h]))
        ribbon += 2 * sum(mins)
        ribbon += l * w * h


    print wrap
    print ribbon





if __name__ == '__main__':
    script, input_file = sys.argv
    main(input_file)
