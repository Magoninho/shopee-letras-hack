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

def has_same_letters(word):
	arr = list(word)
	return len(arr) != len(set(arr))

def filter_by_letters(words, letters):
	result = []
	for word in words:
		counter = 0
		for letter in letters:
			if letter in word and not_other_letters(word, letters):
				counter += 1
		if counter >= 3:
			result.append(word)
				
	return result

def get_repeated_letters(letters):
	newlist = []
	duplist = []
	if has_same_letters(letters):
		for letter in letters:
			if letter not in newlist:
				newlist.append(letter)
			else:
				duplist.append(letter)

	return duplist
				

def remove_words_with_same_letters(words):
	result = []
	for word in words:
		if not has_same_letters(word):
			result.append(word)
	return result

allow = False

with open('palavras_filtradas.txt', 'r') as f:
	words = f.read().splitlines()
	filtered_words = filter_by_letters(words, letters)

	if not allow:
		filtered_words = remove_words_with_same_letters(filtered_words)

	for word in filtered_words:
		print(word)



