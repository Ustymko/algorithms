def get_input_data():
    import re

    input_file = open("wchain.in.txt", "r")
    content = input_file.readlines()
    length = int(content[0])
    words_in_file = []
    for i in content[1:]:
        words_in_file.append(re.findall("[a-z]+", i))
    words = [item for sublist in words_in_file for item in sublist]
    input_file.close()
    return length, words


def write_output_data(max_chain: int):
    output_file = open("wchain.out.txt", "w")
    output_file.write(str(max_chain))
    output_file.close()
