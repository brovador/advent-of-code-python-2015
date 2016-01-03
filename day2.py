#encoding: utf-8
import os

def main():

    script_name = os.path.basename(__file__)
    input_file = './{0}-input.txt'.format(os.path.splitext(script_name)[0])

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
    main()
