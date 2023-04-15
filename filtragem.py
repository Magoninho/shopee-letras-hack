from unidecode import unidecode
import string

def is_distinct_letters(word):
    for i in range(len(word)):
        first_letter = word[i]
        for j in range(len(word) - 1):
            second_letter = word[j]
            if first_letter == second_letter and i != j:
                return False
            else:
                continue
    return True

def has_dots(word):
	invalidcharacters= set(string.punctuation)
	return any(char in invalidcharacters for char in word)


filtered = []
with open('palavras.txt', 'r') as f:
	words = f.read().splitlines()

	for word in words:
		if len(word) <= 5 and len(word) >= 3 and not has_dots(word):
			filtered.append(unidecode(word))
	
with open('palavras_filtradas.txt', 'a') as f:
	for word in filtered:
		f.write(f"{word}\n")

