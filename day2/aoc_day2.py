import sys


def part1(lines):
    forward = 0
    depth = 0
    for line in lines:
        words = line.split()
        if words[0] == 'forward':
            forward += int(words[1])
        elif words[0] == 'down':
            depth += int(words[1])
        elif words[0] == 'up':
            depth -= int(words[1])
    print(str(forward * depth))


def part2(lines):
    forward = 0
    depth = 0
    aim = 0
    for line in lines:
        words = line.split()
        if words[0] == 'forward':
            forward += int(words[1])
            depth += int(words[1]) * aim
        elif words[0] == 'down':
            aim += int(words[1])
        elif words[0] == 'up':
            aim -= int(words[1])
    print(str(forward * depth))


input_file = None

for i in range(0, len(sys.argv)):
    if sys.argv[i] == '-f':
        input_file = open(sys.argv[i + 1], 'r')

lines = input_file.readlines()

part1(lines)
part2(lines)
