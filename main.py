# Caesar Cipher Encrypt/Decrypt
def caesar(message,shift):
	new_message=[]
	letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ "
	message=message.upper()
	for i in message:
		if i in letters:
			index=letters.index(i)
			other_index=(index+shift)%len(letters)
			new_message.append(letters[other_index])
	return ''.join(new_message)
# print(caesar("EDUYMGODFVS RDJSADNYQTWDSZIVDXLIDPECBDHSK",23))


#Vigenere Encrypt
def vigenere_encrypt(text,key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    encrypted = ""
    text = text.upper()
    key = key.upper()
    for i in range(0,len(text)):
        t_index = alphabet.index(text[i])
        k_index = alphabet.index(key[i % len(key)])
        final_index = (t_index % len(alphabet) + k_index % len(alphabet)) % len(alphabet)
        encrypted += alphabet[final_index]
    return encrypted


# Vigenere Decrypt
def vigenere_decrypt(text, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    decrypted = ""
    text = text.upper()
    key = key.upper()
    for i in range(0,len(text)):
        t_index = alphabet.index(text[i])
        k_index = alphabet.index(key[i % len(key)])
        final_index = (t_index % len(alphabet) - k_index % len(alphabet)) % len(alphabet)
        decrypted += alphabet[final_index]
    return decrypted
