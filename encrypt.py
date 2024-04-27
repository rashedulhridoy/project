import random
import string

chars = " " + string.whitespace + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()


random.shuffle(key)


#print(f"chars   : {chars}")
#print(f"key     : {key}")

#Encrypt
plain_text = input("Enter a Passwd To encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]


print(f"orginal message : {plain_text}")
print(f"cipher text : {cipher_text}")

#Decrypt
cipher_text = input("Enter a Passwd To Decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"encrypted text : {cipher_text}")
print(f"orginal message : {plain_text}")
