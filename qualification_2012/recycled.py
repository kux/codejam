import bitarray
import math
import sys


def circular_permutation(number):
    no_digits = int(math.log10(number)) + 1
    for _ in xrange(no_digits):
        last_digit = number % 10
        number = last_digit * 10 ** (no_digits - 1) + number / 10
        yield int(number)
        


def recycle(lower, upper):
    result = 0
    already_parsed = bitarray.bitarray(upper - lower + 1)
    already_parsed.setall(0)
    for number in xrange(lower, upper + 1):
        if already_parsed[number - lower]:
            continue
        permutation_no = 0
        for permutation in circular_permutation(number):
            if permutation < lower or permutation > upper:
                continue
            if not already_parsed[permutation - lower]:
                permutation_no += 1
                already_parsed[permutation - lower] = True
        result += permutation_no * (permutation_no - 1) / 2
    return result

            
def parse_file(input_file): 
    with open(input_file) as f:
        f.readline()  # jump over the 'number of testcases' line
        for i, line in enumerate(f):
            lower, upper = map(int, line.split(' '))
            result = recycle(lower, upper)
            print 'Case #%d: %d' % (i+1, result)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(1)
    # parse_file(sys.argv[1])

    import cProfile
    def run():
        parse_file(sys.argv[1])

    cProfile.run('run()', 'profile_output')
