def get_input_data():
    import re

    file = open("in.txt", "r")
    content = file.readlines()
    file.close()
    pattern = re.findall("[A-Za-z]+", content[0])[0]
    text = re.findall("[A-Za-z]+", content[1])[0]
    return pattern, text


def write_output_data(times_pattern_occurs):
    file = open("out.txt", "w")
    file.write("Occurs ")
    file.write(str(times_pattern_occurs))
    file.write(" times")
    file.close()
