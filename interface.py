from tkinter import *

w = Tk()
w.title('Шифрование')
w.geometry('300x280')

labelframe1 = LabelFrame(text='Данные')
labelframe2 = LabelFrame(text='Зашифрованные сообщение')
text = Label(labelframe1, text='Введите текст:')
key = Label(labelframe1, text='Введите ключ:')
encrypt = Label(labelframe2, text='Шифр Цезаря: ')
encrypt_text = Label(labelframe2)
atbash_encrypt = Label(labelframe2, text='Шифр Атбаш: ')
atbash_encrypt_text = Label(labelframe2)

plaintextbox = Entry(labelframe1)
keybox = Entry(labelframe1, width=5)

button = Button(text='Зашифровать', width=20, command=encrypt)

labelframe1.pack(fill=X, padx=10, pady=5)
labelframe2.pack(fill=X, padx=10, pady=5)
text.grid(row=0, column=0, padx=20, pady=2)
key.grid(row=0, column=1, padx=20, pady=2)
plaintextbox.grid(row=1, column=0, padx=20, pady=8)
keybox.grid(row=1, column=1, padx=20, pady=8)
encrypt.pack(pady=5)
encrypt_text.pack(pady=5)
atbash_encrypt.pack(pady=5)
atbash_encrypt_text.pack(pady=5)
button.pack(pady=3)

if __name__ == '__main__':
    w.mainloop()
