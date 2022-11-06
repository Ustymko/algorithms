from input_output_data import *

# preparing useful variables and lists
length, words = get_input_data()
memoization_arr = []
for i in range(length):
    memoization_arr.append(1)


# recursive max chain function
def max_chain(word: str, current_index: int) -> int:
    if memoization_arr[current_index] > 1:
        return memoization_arr[current_index]

    next_words = []
    for letter_idx in range(len(word)):
        sliced_word = word[:letter_idx] + word[letter_idx + 1:]
        if sliced_word in words:
            next_words.append([sliced_word, words.index(sliced_word)])
    if next_words:
        memoization_arr[current_index] = 1 + max(
            max_chain(word_and_index[0], word_and_index[1]) for word_and_index in next_words)
    return 1


# copy the original list of words into list of starting points
list_of_starting_points = [_ for _ in words]
while list_of_starting_points:
    starting_word = str(min(list_of_starting_points, key=len))
    starting_word_idx = words.index(starting_word)
    list_of_starting_points.remove(starting_word)
    max_chain(starting_word, starting_word_idx)

result = max(memoization_arr)
write_output_data(result)
