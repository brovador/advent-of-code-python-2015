#encoding: utf-8
import sys
import os
import re
import string
from random import shuffle

min_steps = 100
max_steps = 10000
max_score = 0

def main():

    global max_steps

    script_name = os.path.basename(__file__)
    input_file = './{0}-input.txt'.format(os.path.splitext(script_name)[0])

    with open(input_file, 'r') as f:
        commands = [l.strip() for l in f if l.strip() != '']

    def get_molecules(molecules_str):
        r = re.compile('([A-Z][a-z]?)')
        return [x.groups()[0] for x in r.finditer(molecules_str)]

    result_medicine = commands[-1][::-1]
    replacements = commands[:-1]
    replacements_data = {}

    r = re.compile('(\w+) => (\w+)')
    for repl in replacements:
        m = r.match(repl)
        replacements_data[m.groups()[1][::-1]] = m.groups()[0][::-1]
    print replacements_data

    def rep(x):
        return replacements_data[x.group()]

    medicine = result_medicine
    steps = 0
    while medicine != 'e':
        medicine = re.sub('|'.join(replacements_data.keys()), rep, medicine, 1)
        steps += 1
    print steps



            # ra, rb = repl
            # if medicine.find(rb) != -1:
            #     new_medicine = medicine.replace(rb, ra, 1)
            #     #print '{}. {} => {}'.format(steps, medicine, new_medicine)
            #     if new_medicine == 'e':
            #         if steps < min_steps:
            #             min_steps = steps
            #     else:
            #         print len(new_medicine)
            #         make_replacement(new_medicine, steps + 1)

    make_replacement(result_medicine, 1)
    print min_steps

if __name__ == '__main__':
    main()
