#!/usr/bin/python3
"""
This script reads stdin line by line and computes the metrics

"""

import sys

# Store the status codes to track in an array
status_codes = [200, 301, 400, 401, 403, 404, 405, 500]

# Initialize variables to store metrics
total_size = 0
status_code_counts = {str(code): 0 for code in status_codes}
line_count = 0

try:
    for line in sys.stdin:
        # Split the line into parts
        parts = line.split()

        # Check if the line matches the expected format
        if len(parts) != 7:
            continue

        # unpack the elements of parts variable into their separate variables
        ip, date, request, status_code, file_size = parts

        # Parse and update metrics
        try:
            file_size = int(file_size)
            total_size += file_size
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

            line_count += 1

        except ValueError:
            pass

        # Print statistics after every 10 lines
        if line_count % 10 == 0:
            print(f"File size: {total_size}")
            for code in sorted(status_codes):
                if status_code_counts[str(code)] > 0:
                    print(f"{code}: {status_code_counts[str(code)]}")

except KeyboardInterrupt:
    # Handle CTRL+C interruption
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        if status_code_counts[str(code)] > 0:
            print(f"{code}: {status_code_counts[str(code)]}")
