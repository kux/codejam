import sys


def dance(surprises, points, dancers):
    threashold = 3 * points
    winners = 0
    for dancer in dancers:
        if dancer >= threashold - 2:
            winners += 1
        elif dancer >= threashold - 4 and dancer >= 2 and surprises > 0:
            surprises -= 1
            winners += 1
    return winners


def parse_file(input_file):
    with open(input_file) as f:
        f.readline()  # jump over the 'number of testcases' line
        for i, line in enumerate(f):
            entries = [int(entry) for entry in line.split(' ')]
            surprises = entries[1]
            points = entries[2]
            winners = dance(surprises, points, entries[3:])
            print 'Case #%d: %d' % (i+1, winners)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(1)
    parse_file(sys.argv[1])
