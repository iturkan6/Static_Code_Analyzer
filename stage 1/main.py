def find_long(path):
    line_number = 0
    with open(path, "r") as file:
        for line in file:
            line_number += 1
            if len(line) > 79:
                print(f"Line {line_number}: S001 Too long")


def main():
    path = input()
    find_long(path)


if __name__ == "__main__":
    main()
