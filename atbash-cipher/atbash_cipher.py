def encode(plain_text):
	backwards = ""
	i = 0
	while i <= len(plain_text)-1:
		backwards = backwards + plain_text[len(plain_text)-1-i]
		i = i + 1
	print(backwards)
    


def decode(ciphered_text):
	backwards = ""
	i = 0
	while i <= len(ciphered_text)-1:
		backwards = backwards + ciphered_text[len(ciphered_text)-1-i]
		i = i + 1
	print(backwards)
