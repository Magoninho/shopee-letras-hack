from collections import Counter

letters = [
	input(),
	input(),
	input(),
	input(),
	input(),
]


def not_other_letters(word, letters):
	for letter in word:
		if not letter in letters:
			return False
	return True


def filter_by_letters(words, letters):
	result = []
	for word in words:
		counter = 0 # contador de letras
		for letter in letters:
			if letter in word and not_other_letters(word, letters):
				counter += 1

		if counter >= 3:
			if valid_amount_of_letters(word, letters):
				result.append(word)
				
	return result


def get_letter_counter(letters):
	arr = sorted(list(letters))
	return dict(Counter(arr))

# this function checks if the word has the apropriate number of repeated letters 
# accordingly to the input letters
def valid_amount_of_letters(word, letters):
	letter_count_input = get_letter_counter(letters)
	letter_count_word  = get_letter_counter(word)

	for letter in letter_count_word:
		try:
			if (letter_count_word[letter] > letter_count_input[letter]):
				return False
		except KeyError:
			continue

	return True


allow = False

with open('palavras_filtradas.txt', 'r') as f:
	words = f.read().splitlines()
	filtered_words = filter_by_letters(words, letters)


	for word in filtered_words:
		print(word)



