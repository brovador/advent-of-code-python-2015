#encoding: utf-8
import sys
import os
import re


class Emulator():
    def __init__(self):
        self.a = 1
        self.b = 0
        self.pc = 0
        self.instructions = [
            ('hlf (\w)', '_exec_hlf'),
            ('tpl (\w)', '_exec_tpl'),
            ('inc (\w)', '_exec_inc'),
            ('jmp ([+-]\d+)', '_exec_jmp'),
            ('jie (\w), ([+-]\d+)', '_exec_jie'),
            ('jio (\w), ([+-]\d+)', '_exec_jio'),
        ]

    def execute_program(self, prog):
        self.pc = 0
        prog = prog.split('\n')

        while self.pc < len(prog):
            instruction = prog[self.pc]
            for i in self.instructions:
                match = re.match(i[0], instruction)
                if match:
                    getattr(self, i[1])(*match.groups())
                    break


    def _exec_hlf(self, r):
        setattr(self, r, int(getattr(self, r) // 2))
        self.pc += 1

    def _exec_tpl(self, r):
        setattr(self, r, getattr(self, r) * 3)
        self.pc += 1

    def _exec_inc(self, r):
        setattr(self, r, getattr(self, r) + 1)
        self.pc += 1

    def _exec_jmp(self, offset):
        self.pc += int(offset)

    def _exec_jie(self, r, offset):
        if getattr(self, r) % 2 == 0:
            self.pc += int(offset)
        else:
            self.pc += 1

    def _exec_jio(self, r, offset):
        if getattr(self, r) == 1:
            self.pc += int(offset)
        else:
            self.pc += 1


def main():
    global min_mana_spent

    script_name = os.path.basename(__file__)
    input_file = './{0}-input.txt'.format(os.path.splitext(script_name)[0])

    with open(input_file, 'r') as f:
        commands = f.read().strip()

    emu = Emulator()
    emu.execute_program(commands)
    print emu.a, emu.b





if __name__ == '__main__':
    main()
