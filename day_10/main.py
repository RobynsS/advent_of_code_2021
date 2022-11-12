import statistics


def read_data(filename):
    with open(filename) as f:
        data = [line for line in f.read().splitlines()]
    return data


def reverse(bracket):
    if bracket in ["(", "[", "{", "<", ")", "]", "}", ">"]:
        if bracket == "(":
            return ")"
        if bracket == ")":
            return "("
        if bracket == "[":
            return "]"
        if bracket == "{":
            return "}"
        if bracket == "]":
            return "["
        if bracket == "}":
            return "{"
        if bracket == "<":
            return ">"
        if bracket == ">":
            return "<"
    else:
        raise ValueError("Incorrect character")


def get_illegal_bracket(data):
    stack = []
    for char in data:
        if char in ["(", "[", "{", "<"]:
            stack.append(char)
        else:
            if reverse(char) != stack[-1]:
                return char
            else:
                stack.pop()

    return None


def get_closing_brackets(data):
    stack = []
    for char in data:
        if char in ["(", "[", "{", "<"]:
            stack.append(char)
        else:
            if reverse(char) != stack[-1]:
                return None
            else:
                stack.pop()
    stack.reverse()
    return [reverse(x) for x in stack]


def count_score_illegal(chars):
    count = 0
    for char in chars:
        if char == ")":
            count += 3
        elif char == "}":
            count += 1197
        elif char == "]":
            count += 57
        elif char == ">":
            count += 25137
    return count


def count_score_incomplete(lines):
    def score_char(charac):
        if charac == ")":
            return 1
        if charac == "]":
            return 2
        if charac == "}":
            return 3
        if charac == ">":
            return 4

    counts = []

    for line in lines:
        count = 0
        for char in line:
            count *= 5
            count += score_char(char)
        counts.append(count)

    return counts


def main():
    data = read_data("input.txt")
    illegal_chars = []
    closing_lines = []
    for line in data:
        char = get_illegal_bracket(line)
        closing_chars = get_closing_brackets(line)
        if char is not None:
            illegal_chars.append(char)
        if closing_chars is not None:
            closing_lines.append(closing_chars)
    print(count_score_illegal(illegal_chars))
    counts = count_score_incomplete(closing_lines)
    counts.sort()
    print(statistics.median(counts))


if __name__ == "__main__":
    main()
