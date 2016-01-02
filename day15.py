#encoding: utf-8
import sys
import os
import re
import operator

def main():
    script_name = os.path.basename(__file__)
    input_file = './{0}-input.txt'.format(os.path.splitext(script_name)[0])

    with open(input_file, 'r') as f:
        commands = [l.strip() for l in f]

    data = {}
    r = re.compile(r'(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)')
    for c in commands:
        props = r.match(c).groups()
        data[props[0]] = tuple([int(x) for x in props[1:]])

    def compute_recipe(amounts):
        r = [0] * 5
        for i, p in data.iteritems():
           r = map(sum, zip(r, [x * amounts[i] for x in p]))
        for i, x in enumerate(r):
            r[i] = x if x > 0 else 0
        return reduce(lambda x, y: x * y, r[:-1])

    def compute_calories(amounts):
        r = 0
        for i, p in data.iteritems():
            r += p[-1] * amounts[i]
        return r

    def gen_serie(num):
        if num == 0:
            return [0]
        arr = []
        base = 100
        while num:
            rem = num % base
            num = num // base
            arr.append(rem)
        arr.reverse()
        return arr

    def teaspoons(l):
        i = 0
        r = gen_serie(i)
        while len(r) <= l:
            if sum(r) == 100:
                yield r + [0] * (l - len(r))
            i += 1
            r = gen_serie(i)

    gen = teaspoons(len(data.keys()))
    best_score = 0
    best_result = None
    ingredients = data.keys()
    while True:
        try:
            r = gen.next()
        except:
            break

        amounts = {}
        for i in range(len(ingredients)):
            amounts[ingredients[i]] = r[i]
        s = compute_recipe(amounts)
        if s > best_score and compute_calories(amounts) == 500:
            best_score = s
            best_result = amounts
    print best_score
    print best_result


if __name__ == '__main__':
    main()
