import os
import tkinter as tk
from tkinter import filedialog

def c():
    print("______________________________________________________________________________________________")
def menu0():
    c()
    menu = "1-Nueva lectura ","2-Salir "
    return menu
def selectFile():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename()
def read():
    file = selectFile()
    print("Leyendo "+file)
    import pytesseract
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    from PIL import Image
    from pytesseract import image_to_string
    texto = image_to_string(Image.open(file))
    
    print("## LECTURA COMPLETADA")
    file = filedialog.asksaveasfile(mode='w', defaultextension=".txt", filetypes=(("TXT file", "*.txt"),("All Files", "*.*") ))
    if file is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    file.write(texto)
    file.close() # `()` was missing.

def analize(x):
    salir1 = False
    if x == '1':
        while not salir1:
            print(read())
            comando = input("Nueva Lectura >")
            analize(comando)
salir = False;
while not salir:
    print(menu0())
    comando = input(">")
    read()


