#!/usr/bin/python3
import sys
import signal
import re

total_file_size = 0
status_counts = {
    200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
}
line_count = 0

log_pattern = re.compile(r'^(\S+) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$')

def print_stats():
    print("File size: {}".format(total_file_size))
    for status in sorted(status_counts):
        if status_counts[status] > 0:
            print("{}: {}".format(status, status_counts[status]))

def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        match = log_pattern.match(line)
        if match:
            ip, date, status_code, file_size = match.groups()
            try:
                status_code = int(status_code)
                file_size = int(file_size)
            except ValueError:
                continue

            if status_code in status_counts:
                status_counts[status_code] += 1
                total_file_size += file_size
                line_count += 1

            if line_count % 10 == 0:
                print_stats()
except Exception as e:
    print(f"An error occurred: {e}")

print_stats()

