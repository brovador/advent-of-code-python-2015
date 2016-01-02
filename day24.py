#encoding: utf-8
import sys
import os
import re
import itertools
from operator import mul

def main():
    global min_mana_spent

    script_name = os.path.basename(__file__)
    input_file = './{0}-input.txt'.format(os.path.splitext(script_name)[0])

    with open(input_file, 'r') as f:
        commands = [x for x in f]

    packages = [int(x) for x in commands]

    packages = sorted(packages)[::-1]
    num_packages = 4
    group_weight = sum(packages) / num_packages
    min_group_len = int(group_weight / max(packages)) + 1


    def is_solution(sol, packages, groups):
        result = False
        _packages = [p for p in packages if p not in sol]
        for i in range(min_group_len, len(_packages)):
            for x in itertools.combinations(_packages, i):
                if sum(x) == group_weight:
                    if groups > 2:
                        result = is_solution(x, _packages, groups - 1)
                    else:
                        result = True
                    break
            if result:
                break
        return result

    result = None
    for i in range(min_group_len, len(packages)):
        for x in itertools.combinations(packages, i):
            if sum(x) == group_weight and is_solution(x, packages, num_packages - 1):
                qe = reduce(mul, x)
                if not result or qe < result[1]:
                    result = (x, qe)
        if result:
            break

    print result

if __name__ == '__main__':
    main()
