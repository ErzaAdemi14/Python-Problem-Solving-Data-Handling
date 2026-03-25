def find_longest_line(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()

            if len(lines) == 0:
                return "File is empty."

            longest_line = max(lines, key=len)
            return longest_line.strip()

    except FileNotFoundError:
        return "File not found."


print(find_longest_line("sample.txt"))
print(find_longest_line("missing.txt"))
print(find_longest_line("empty.txt"))