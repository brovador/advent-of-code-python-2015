#encoding: utf-8
import sys
import os
import re

best_distance = 0
best_route = None

def main():
    script_name = os.path.basename(__file__)
    input_file = './{0}-input.txt'.format(os.path.splitext(script_name)[0])

    with open(input_file, 'r') as f:
        commands = [l.strip() for l in f]

    def look_and_say(nums):
        out = []
        current = nums[0]
        repeats = 1
        for n in nums[1:]:
            if n == current:
                repeats += 1
            else:
                out.append(repeats)
                out.append(current)
                current = n
                repeats = 1
        out.append(repeats)
        out.append(current)
        return out

    out = [int(x) for x in commands[0]]
    for i in range(50):
        out = look_and_say(out)
    print len(out)







if __name__ == '__main__':
    main()
