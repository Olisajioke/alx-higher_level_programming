#!/usr/bin/python3
"""Reads from standard input and computes metrics.

This script processes input lines and calculates statistics.
After every ten lines or upon receiving a keyboard interruption (CTRL + C),
it prints the following metrics:
    - Total accumulated file size.
    - Counts of encountered status codes.

Note: The function name 'print_stats' is retained as per the request.
"""


def print_stats(file_size, status_counts):
    """Print accumulated metrics.

    Args:
        file_size (int): The total accumulated file size.
        status_counts (dict): Counts of encountered status codes.
    """
    print("Total file size up to this point: {}".format(file_size))
    for code, count in sorted(status_counts.items()):
        print("Status code {}: {}".format(code, count))


if __name__ == "__main__":
    import sys

    file_size = 0
    status_counts = {}
    status_quo = ['200', '301', '400', '401', '403', '404', '405', '500']
    line_count = 0

    try:
        for line in sys.stdin:
            if line_count == 10:
                print_stats(file_size, status_counts)
                line_count = 1
            else:
                line_count += 1

            elements = line.split()

            try:
                size = int(elements[-1])
                file_size += size
            except (IndexError, ValueError):
                pass

            try:
                status_code = elements[-2]
                if status_code in status_quo:
                    if status_code in status_counts:
                        status_counts[status_code] += 1
                    else:
                        status_counts[status_code] = 1
            except IndexError:
                pass

        print_stats(file_size, status_counts)

    except KeyboardInterrupt:
        print_stats(file_size, status_counts)
        raise
