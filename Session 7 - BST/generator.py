import random
import string

def insert_lines(input_file, output_file1):
    with open(input_file, 'r') as f:
        strings = f.readlines()

    selected_strings = random.sample(strings, 100000)

    with open(output_file1, 'w') as f:
        f.writelines(selected_strings)


def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


random_strings1 = [generate_random_string(8) + " " + str(random.randint(100_000_000, 999_999_999)) for i in range(1000000)]
random_strings4 = [generate_random_string(8) + " " + str(random.randint(100_000_000, 999_999_999)) for i in range(100000)]


with open("db.txt", 'w') as f:
    for s in random_strings1:
        f.write(s + '\n')


with open("query2.txt", 'w') as f:
    for s in random_strings4:
        f.write(s + '\n')

insert_lines("db.txt", "query1.txt")
