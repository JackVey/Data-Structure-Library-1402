import random
import string

quantity = 600_000
def insert_lines(input_file, output_file1):
    with open(input_file, 'r') as f:
        strings = f.readlines()

    selected_strings = random.sample(strings, quantity//10)

    with open(output_file1, 'w') as f:
        f.writelines(selected_strings)


def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


random_strings1 = [generate_random_string(8) + " " + str(random.randint(100_000_000, 999_999_999)) for i in range(quantity)]
# random_strings4 = [generate_random_string(8) + " " + str(random.randint(100_000_000, 999_999_999)) for i in range(100000)]


with open("db.txt", 'w') as f:
    for s in random_strings1:
        f.write(s + '\n')


# with open("query2.txt", 'w') as f:
#     for s in random_strings4:
#         f.write(s + '\n')

insert_lines("db.txt", "query1.txt")

def process_file(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    sorted_lines = sorted(lines, key=lambda x: x.split()[0])

    with open(output_file, 'w') as f:
        i = 0
        while i < len(sorted_lines):
            range_size = random.randint(10, 50)
            end = min(i + range_size, len(sorted_lines))

            reversed_lines = sorted_lines[i:end][::-1]
            f.writelines(reversed_lines)

            i = end

process_file("db.txt", "db2.txt")
