import interface
from ciphers import caesar_encrypt
from ciphers2 import atbash_encrypt
def encrypt():
    plaintext = interface.plaintextbox.get()
    key = int(interface.keybox.get())
    enc = caesar_encrypt(plaintext, key)
    atb_enc = atbash_encrypt(plaintext)
    interface.encrypt_text.config(text=enc)
    interface.atbash_encrypt_text.config(text=atb_enc)
interface.button.config(command=encrypt)
interface.w.mainloop()

