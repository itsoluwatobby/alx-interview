#!/usr/bin/python3
"""
Write a script that reads stdin line by line and computes metrics:
"""
import sys


def print_result(total_file_size, status_codes):
    """Prints the final file result"""
    print('File size: {:d}'.format(total_file_size))
    sorted_keys = sorted(status_codes.keys())
    for key in sorted_keys:
        value = status_codes[key]
        if value != 0:
            print('{}: {}'.format(key, value))


def main():
    """Runs the main program"""
    i = 0
    total_file_size = 0
    status_codes = {
                    '200': 0,
                    '301': 0,
                    '400': 0,
                    '401': 0,
                    '403': 0,
                    '404': 0,
                    '405': 0,
                    '500': 0
                   }

    try:
        for line in sys.stdin:
            args = line.split(' ')
            if len(args) > 2:
                status_line = args[-2]
                file_size = args[-1]
                if status_line in status_codes:
                    status_codes[status_line] += 1
                total_file_size += int(file_size)
                i += 1
                if i == 10:
                    print_result(total_file_size, status_codes)
                    i = 0
    except KeyboardInterrupt:
        pass
    finally:
        print_result(total_file_size, status_codes)


if __name__ == '__main__':
    main()
