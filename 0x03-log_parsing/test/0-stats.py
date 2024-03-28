#!/usr/bin/python3

import sys

def print_statistics(total_size, status_counts):
    print(f"File size: {total_size}")
    for status_code, count in sorted(status_counts.items()):
        print(f"{status_code}: {count}")

def main():
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            parts = line.split()
            if len(parts) >= 9 and parts[-2].isdigit():
                status_code = int(parts[-2])
                file_size = int(parts[-1])
                total_size += file_size
                if status_code in status_counts:
                    status_counts[status_code] += 1

                line_count += 1
                if line_count % 10 == 0:
                    print_statistics(total_size, status_counts)
    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)

if __name__ == "__main__":
    main()
