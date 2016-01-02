#encoding: utf-8
import sys
import os

def main():
    script_name = os.path.basename(__file__)
    input_file = './{0}-input.txt'.format(os.path.splitext(script_name)[0])

    with open(input_file, 'r') as f:
        words = [l.strip() for l in f]

    nice_count = 0
    for w in words:
        #nice = len([x for x in w if x in 'aeiou']) >= 3
        #nice = nice and reduce(lambda x, y: True if (x == y or x == True) else y, w) == True
        #nice = nice and all(map(lambda x: x not in w, ['ab', 'cd', 'pq', 'xy']))

        def nice1(w):
            nice = False
            for i in range(len(w) - 3):
                nice = nice or w[i:i+2] in w[i+2:]
            return nice

        def nice2(w):
            nice = False
            for i in range(len(w) - 2):
                nice = nice or w[i] == w[i + 2]
            return nice

        nice = nice1(w) and nice2(w)
        nice_count += 1 if nice else 0

    print nice_count



if __name__ == '__main__':
    main()
