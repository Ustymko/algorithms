def unpack():
    import re

    file = open("career.in.txt", "r")
    content = file.readlines()
    number_of_levels = int(re.findall("\\d+", content[0])[0])
    positions = []
    for line in content[1:]:
        positions.append(list(map(int, re.findall("\\d+", line))))
    return number_of_levels, positions


def output(max_experience: int):
    output_file = open("career.out.txt", "w")
    output_file.write(str(max_experience))
    output_file.close()
