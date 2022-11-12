from input_output_data import *

# preparing useful variables and lists
length, words = get_input_data()
memoization_arr = []
for i in range(length):
    memoization_arr.append(0)
result = 0


# recursive max chain function
def max_chain(word: str, current_index: int) -> int:
    if memoization_arr[current_index] > 0:
        return memoization_arr[current_index]

    next_words = []
    for letter_idx in range(len(word)):

        sliced_word = word[:letter_idx] + word[letter_idx + 1:]
        if sliced_word in words:
            next_words.append([sliced_word, words.index(sliced_word)])
    if next_words:
        current_result = 1 + max(
            max_chain(word_and_index[0], word_and_index[1]) for word_and_index in next_words)
        memoization_arr[current_index] = current_result
        return current_result
    return 1


for i in range(len(words)):
    temp_result = max_chain(words[i], i)
    if temp_result > result:
        result = temp_result

# result = max(memoization_arr)
write_output_data(result)
