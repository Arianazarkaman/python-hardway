from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("first let's print the whole file\n")

print_all(current_file)

print("now let's rewind, kind of like a tape.")

rewind(current_file)
