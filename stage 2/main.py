from pathlib import Path


def line_too_long(line: str) -> bool:
    return len(line) > 79


def wrong_indentation_basic(line: str) -> bool:
    return line.index(line.lstrip()) % 4 != 0


def semicolon_after_statement(line: str) -> bool:
    return line.split("#")[0].rstrip().endswith(";")


def bad_spacing_before_comment(line: str) -> bool:
    return (
        not line.startswith("#")
        and "#" in line
        and not line.split("#")[0].endswith("  ")
    )


def todo_comment_found(line: str) -> bool:
    return "#" in line and "todo" in line.split("#")[1].lower()


line_checks = {
    line_too_long: ("S001", "Line is too long"),
    wrong_indentation_basic: ("S002", "Indentation is not a multiple of four"),
    semicolon_after_statement: ("S003", "Unnecessary semicolon after a statement"),
    bad_spacing_before_comment: ("S004", "Less than two spaces before inline comment"),
    todo_comment_found: ("S005", "TODO comment found"),
}


def error_msg(n_line: int, errcode: str, msg: str) -> str:
    return f"Line {n_line}: {errcode} {msg}"


with open(Path(input())) as file:
    prev_blank_lines = 0
    for i, line in enumerate(file, 1):
        for check, (errcode, msg) in line_checks.items():
            if check(line):
                print(error_msg(i, errcode, msg))

        if line.isspace():
            prev_blank_lines += 1
        elif prev_blank_lines > 2:
            prev_blank_lines = 0
            print(error_msg(i, "S006", "Too many blank lines"))