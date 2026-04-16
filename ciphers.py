
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
def caesar_encrypt(plaintext, key):
    plaintext = plaintext.lower()
    ciphertext = ''
    for i in plaintext:
        if ' ' in i:
            ciphertext+=' '
        else:
            index = alphabet.find(i)
            new_index = index+key
            new_index = new_index%len(alphabet)
            new_letter = alphabet[new_index]
            ciphertext += new_letter
    return ciphertext
'''k = 0
for a in range(0,33):
    k -= 1
    print(caesar_encrypt('ч жбъщиуоюя ёхэ цищъз нюйё хзцхн', k))'''

       
