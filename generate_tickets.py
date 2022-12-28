import argparse
import hashlib


def hash_text(text, salt):
    return hashlib.sha256((str(salt) + text).encode()).hexdigest()


def generate_distribution(students, numbilets, salt):
    for student in students:
        print(f'{student}: {int(hash_text(student, salt), 16) % numbilets + 1}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--file', type=str, help='file with students', required=True)
    parser.add_argument('--numbilets', type=int, help='number of tickets', required=True)
    parser.add_argument('--parameter', type=int, help='magic parameter', required=True)

    args = parser.parse_args()

    with open(args.file) as f:
        students = [student.rstrip() for student in f]

    generate_distribution(students, args.numbilets, args.parameter)
