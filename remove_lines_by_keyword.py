# Remove Line containing Keywors.
# Useful for Log Parsing
import sys

if len(sys.argv) < 3:
    print("Usage: python remove_lines.py <keyword1> <keyword2> ... <input_file> <output_file>")
    sys.exit(1)

keywords = sys.argv[1:-2]
input_file = sys.argv[-2]
output_file = sys.argv[-1]

try:
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    with open(output_file, 'w') as outfile:
        for line in lines:
            if not any(keyword in line for keyword in keywords):
                outfile.write(line)

    print(f"Lines containing specified keywords have been removed and saved to {output_file}.")
except FileNotFoundError:
    print(f"File {input_file} not found.")
