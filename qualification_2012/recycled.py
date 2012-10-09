import copy
import sys


def circular_permutation(number):
    for _ in xrange(len(number)):
        number = '%s%s' % (number[-1], number[:-1])
        yield number
        


def recycle(lower, upper):
    result = 0
    numbers_set = set(str(x) for x in xrange(lower, upper + 1))
    for number in copy.copy(numbers_set):
        if number not in numbers_set:
            continue
        permutation_no = 0
        for permutation in circular_permutation(number):
            if permutation in numbers_set:
                permutation_no += 1
                numbers_set.remove(permutation)
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
    parse_file(sys.argv[1])

    # import cProfile
    # def run():
    #     parse_file(sys.argv[1])

    # cProfile.run('run()', 'profile_output')
