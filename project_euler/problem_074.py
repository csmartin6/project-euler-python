import sys
from timeit import default_timer as timer
import utils

digit_factorials = [i for i in utils.factorials_(9)]


def problem_074():
    n = 1000000

    cycles = {}
    target_len = 60
    count = 0
    for i in range(1, n):
        cycle_found = False
        curr_num = i
        sequence = {curr_num: 0}
        idx = 1
        while not cycle_found and idx <= target_len:
            next_num = sum([digit_factorials[x] for x in utils.as_digit_array(curr_num)])

            if next_num in sequence:
                cycle_found = True
                cycles[i] = idx
                if idx == target_len:
                    count += 1
                cycles[next_num] = idx - sequence[next_num]

            elif next_num in cycles:
                cycle_found = True
                seq_len = idx + cycles[next_num]
                cycles[i] = seq_len
                if seq_len == target_len:
                    count += 1
            else:
                sequence[next_num] = idx
                idx += 1
                curr_num = next_num

    return count


def main():
    print("Problem 74")
    start = timer()
    print("Answer: {}".format(problem_074()))
    print("Elapsed time: {}".format(timer() - start))


if __name__ == '__main__':
    sys.exit(main())
