#!/usr/bin/python3
import sys
import signal


# Initialize variables to store statistics
file_size = 0
status_code_counts = {}
line_count = 0


# Function to print statistics
def print_statistics():
    global file_size
    global status_code_counts
    print(f"File size: {file_size}")
    for status_code in sorted(status_code_counts.keys()):
        print(f"{status_code}: {status_code_counts[status_code]}")


# Handle SIGINT (Ctrl+C) to print statistics and continue
def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


try:
    for line in sys.stdin:
        # Split the line into parts
        parts = line.split()
        if len(parts) >= 7:
            # Extract the status code and file size
            status_code = parts[-2]
            file_size += int(parts[-1])

            # Update the status code counts
            if status_code.isdigit():
                status_code = int(status_code)
                if status_code in (200, 301, 400, 401, 403, 404, 405, 500):
                    status_code_counts[status_code] = status_code_counts.get(
                            status_code, 0) + 1

            line_count += 1

            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print_statistics()

except KeyboardInterrupt:
    # Handle Ctrl+C to print final statistics
    print_statistics()
