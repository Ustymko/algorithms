def unpack():
    import re

    file = open("input.txt", "r")
    content = file.readlines()
    width, height = re.findall("\\d+", content[0])
    start_i, start_j = re.findall("\\d+", content[1])
    color_to_repaint = re.findall("[A-Z]", content[2])[0]
    colors_field = []
    for i in content[3:]:
        colors_field.append(re.findall("[A-Z]", i))
    return int(width), int(height), int(start_i), int(start_j), str(color_to_repaint), colors_field


def output(data):
    output_file = open("output.txt", "w")
    for i in range(len(data)):
        if i < len(data) - 1:
            output_file.write(str(data[i]) + ",\n")
        else:
            output_file.write(str(data[i]))
    output_file.close()
