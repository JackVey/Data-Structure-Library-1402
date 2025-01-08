import random


def generate_files(N, M):
    D = M // N

    db_ranges = [
        (D // 2, D),
        (D // 2, 2 * D),
        (3 * D // 4, 3 * D)
    ]

    for i in range(1, 4):
        filename = f"DB{i}.txt"
        p, q = db_ranges[i - 1]
        with open(filename, "w") as f:
            for _ in range(N):
                a = random.randint(0, M)
                w = random.randint(p, q)
                b = a + w
                f.write(f"{a} {b}\n")

    for i in range(1, 4):
        filename = f"Query{i}.txt"
        p, q = db_ranges[i - 1]
        with open(filename, "w") as f:
            for _ in range(N // 10):
                a = random.randint(0, M)
                w = random.randint(p, q)
                b = a + w
                f.write(f"{a} {b}\n")


N = 100000
M = 10 ** 10

generate_files(N, M)
