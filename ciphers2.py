alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
def atbash_encrypt(plaintext):
    plaintext = plaintext.lower()
    ciphertext = ''
    for a in plaintext:
        if ' ' in a:
            ciphertext+=' '
        else:
            index = alphabet.find(a)
            new_letter = alphabet[::-1][index]
            ciphertext += new_letter
    return ciphertext
