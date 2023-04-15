from collections import Counter
from unidecode import unidecode
import os

os.system('cls' if os.name == 'nt' else 'clear')

print("""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡏⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿
⣿⣿⣿⣿⣿⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠁⠀⣿
⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠙⠿⠿⠿⠻⠿⠿⠟⠿⠛⠉⠀⠀⠀⠀⠀⣸⣿
⣿⣿⣿⣿⣿⣿⣷⣄⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣴⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⢰⣹⡆⠀⠀⠀⠀⠀⠀⣭⣷⠀⠀⠀⠸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠈⠉⠀⠀⠤⠄⠀⠀⠀⠉⠁⠀⠀⠀⠀⢿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⢾⣿⣷⠀⠀⠀⠀⡠⠤⢄⠀⠀⠀⠠⣿⣿⣷⠀⢸⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡀⠉⠀⠀⠀⠀⠀⢄⠀⢀⠀⠀⠀⠀⠉⠉⠁⠀⠀⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿
┌───────────────────────────┐
│ Hack para jogos de letras │
│ ───────────────────────── │
│ by Magoninho              │
└───────────────────────────┘
""")

t = int(input("Quantas letras? "))

letters = [
	unidecode(input("Insira uma das letras >> "), 'ç') for _ in range(t)
]

# allow = True if int(input("Permitir repetição? 1-sim 2-não(padrão) ")) == 1 else False

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
			# once a word is found, check to see if it has a valid amount of letters
			# remove this conditional to accept words with any amount of repeated letters
			if valid_amount_of_letters(word, letters):
				result.append(word)
				
	return result


# This function returns the number of repetitions of each letter in an array
def get_letter_count(letters):
	arr = sorted(list(letters))
	return dict(Counter(arr))

# this function checks if the word has the apropriate number of repeated letters 
# accordingly to the input letters. E.g. The word "errar" and the input ['a', 'e', 'r', 'r', 'g']
# this will return False, since "errar" has the letter 'r' 3 times, and the input only has 2 times.
def valid_amount_of_letters(word, letters):
	letter_count_input = get_letter_count(letters)
	letter_count_word  = get_letter_count(word)

	for letter in letter_count_word:
		try:
			if (letter_count_word[letter] > letter_count_input[letter]):
				return False
		except KeyError:
			continue

	return True

with open('palavras_filtradas.txt', 'r') as f:
	words = f.read().splitlines()
	filtered_words = filter_by_letters(words, letters)

	os.system('cls' if os.name == 'nt' else 'clear')
	for word in filtered_words:
		print(word)



