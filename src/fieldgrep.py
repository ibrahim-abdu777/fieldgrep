"""Find records matching a plain substring."""


def matches(lines, needle):
    return [line for line in lines if needle in line]


def matches_file(path, needle):
    with open(path, "r", encoding="utf-8", errors="replace") as handle:
        return matches(handle, needle)
