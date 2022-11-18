pattern = "ATNAAAABTT"
text = "ATNAAAABTT"

is_found = False
current_text_index = len(pattern) - 1
while current_text_index < len(text):
    current_pattern_index = len(pattern) - 1
    temp_match = ""
    for i in range(current_text_index, current_text_index - len(pattern) - 2, -1):
        if text[i] == pattern[current_pattern_index]:
            temp_match = pattern[current_pattern_index] + temp_match
            if len(temp_match) == len(pattern):
                break
        else:
            step = 0
            j = current_pattern_index
            while j >= 0:
                if text[i] == pattern[j]:
                    step = len(pattern) - len(temp_match) - j - 1
                    break
                j -= 1
            if j == -1:
                step = len(pattern) - len(temp_match)
            current_text_index += step
            break
        current_pattern_index -= 1
    if temp_match == pattern:
        is_found = not is_found
        break

print(is_found)
