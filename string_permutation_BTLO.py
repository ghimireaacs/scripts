import itertools

num_strings = int(input("How many strings do you want to input? "))

strings = []

for i in range(num_strings):
    string = input(f"Enter string {i + 1}: ")
    strings.append(string)

permutations = list(itertools.permutations(strings))

print("\nAll permutations:")
for p in permutations:
    print(", ".join(p))
