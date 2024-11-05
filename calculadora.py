import tkinter as tk
from tkinter import ttk

campo_activo = "decimal"

def validar_decimal(char):
    return char.isdigit() or char == ''

def validar_binario(char):
    return all(c in '01' for c in char) or char == ''

def validar_octal(char):
    return all(c in '01234567' for c in char) or char == ''

def validar_hexadecimal(char):
    return all(c in '0123456789ABCDEFabcdef' for c in char) or char == ''

def convertir_desde_decimal(event=None):
    try:
        decimal = entrada_decimal.get()
        if decimal:
            decimal = int(decimal)
            entrada_binario.delete(0, tk.END)
            entrada_binario.insert(0, bin(decimal)[2:])
            entrada_octal.delete(0, tk.END)
            entrada_octal.insert(0, oct(decimal)[2:])
            entrada_hexadecimal.delete(0, tk.END)
            entrada_hexadecimal.insert(0, hex(decimal)[2:].upper())
        else:
            limpiar_entradas()
    except ValueError:
        limpiar_entradas()

def convertir_desde_binario(event=None):
    try:
        binario = entrada_binario.get()
        if binario:
            decimal = int(binario, 2)
            entrada_decimal.delete(0, tk.END)
            entrada_decimal.insert(0, str(decimal))
            entrada_octal.delete(0, tk.END)
            entrada_octal.insert(0, oct(decimal)[2:])
            entrada_hexadecimal.delete(0, tk.END)
            entrada_hexadecimal.insert(0, hex(decimal)[2:].upper())
        else:
            limpiar_entradas()
    except ValueError:
        limpiar_entradas()

def convertir_desde_octal(event=None):
    try:
        octal = entrada_octal.get()
        if octal:
            decimal = int(octal, 8)
            entrada_decimal.delete(0, tk.END)
            entrada_decimal.insert(0, str(decimal))
            entrada_binario.delete(0, tk.END)
            entrada_binario.insert(0, bin(decimal)[2:])
            entrada_hexadecimal.delete(0, tk.END)
            entrada_hexadecimal.insert(0, hex(decimal)[2:].upper())
        else:
            limpiar_entradas()
    except ValueError:
        limpiar_entradas()

def convertir_desde_hexadecimal(event=None):
    try:
        hexadecimal = entrada_hexadecimal.get()
        if hexadecimal:
            decimal = int(hexadecimal, 16)
            entrada_decimal.delete(0, tk.END)
            entrada_decimal.insert(0, str(decimal))
            entrada_binario.delete(0, tk.END)
            entrada_binario.insert(0, bin(decimal)[2:])
            entrada_octal.delete(0, tk.END)
            entrada_octal.insert(0, oct(decimal)[2:])
        else:
            limpiar_entradas()
    except ValueError:
        limpiar_entradas()

def limpiar_entradas():
    entrada_decimal.delete(0, tk.END)
    entrada_binario.delete(0, tk.END)
    entrada_octal.delete(0, tk.END)
    entrada_hexadecimal.delete(0, tk.END)

def borrar_ultimo_caracter():
    if campo_activo == "decimal":
        actual = entrada_decimal.get()
        if actual:
            entrada_decimal.delete(len(actual) - 1, tk.END)
            convertir_desde_decimal()
    elif campo_activo == "binario":
        actual = entrada_binario.get()
        if actual:
            entrada_binario.delete(len(actual) - 1, tk.END)
            convertir_desde_binario()
    elif campo_activo == "octal":
        actual = entrada_octal.get()
        if actual:
            entrada_octal.delete(len(actual) - 1, tk.END)
            convertir_desde_octal()
    elif campo_activo == "hexadecimal":
        actual = entrada_hexadecimal.get()
        if actual:
            entrada_hexadecimal.delete(len(actual) - 1, tk.END)
            convertir_desde_hexadecimal()

def enfocar_binario():
    global campo_activo
    campo_activo = "binario"
    entrada_binario.focus()

def enfocar_octal():
    global campo_activo
    campo_activo = "octal"
    entrada_octal.focus()

def enfocar_hexadecimal():
    global campo_activo
    campo_activo = "hexadecimal"
    entrada_hexadecimal.focus()

def enfocar_decimal():
    global campo_activo
    campo_activo = "decimal"
    entrada_decimal.focus()

def insertar_numero(num):
    if campo_activo == "decimal":
        entrada_decimal.insert(tk.END, num)
        convertir_desde_decimal()
    elif campo_activo == "binario" and num in '01':
        entrada_binario.insert(tk.END, num)
        convertir_desde_binario()
    elif campo_activo == "octal" and num in '01234567':
        entrada_octal.insert(tk.END, num)
        convertir_desde_octal()
    elif campo_activo == "hexadecimal" and num in '0123456789ABCDEF':
        entrada_hexadecimal.insert(tk.END, num)
        convertir_desde_hexadecimal()

root = tk.Tk()
root.title("Calculadora de Sistemas Numéricos Automática")

style = ttk.Style(root)
style.configure('TButton', font=('Arial', 10), padding=5)
style.configure('TEntry', font=('Arial', 12), padding=5)
style.configure('TLabel', font=('Arial', 12), padding=5)

vcmd_decimal = (root.register(validar_decimal), '%P')
vcmd_binario = (root.register(validar_binario), '%P')
vcmd_octal = (root.register(validar_octal), '%P')
vcmd_hexadecimal = (root.register(validar_hexadecimal), '%P')

ttk.Label(root, text="Decimal").grid(row=0, column=0, padx=10, pady=10)
entrada_decimal = ttk.Entry(root, validate="key", validatecommand=vcmd_decimal)
entrada_decimal.grid(row=0, column=1, padx=10, pady=10, columnspan=2)
entrada_decimal.bind("<KeyRelease>", convertir_desde_decimal)

ttk.Label(root, text="Binario").grid(row=1, column=0, padx=10, pady=10)
entrada_binario = ttk.Entry(root, validate="key", validatecommand=vcmd_binario)
entrada_binario.grid(row=1, column=1, padx=10, pady=10, columnspan=2)
entrada_binario.bind("<KeyRelease>", convertir_desde_binario)

ttk.Label(root, text="Octal").grid(row=2, column=0, padx=10, pady=10)
entrada_octal = ttk.Entry(root, validate="key", validatecommand=vcmd_octal)
entrada_octal.grid(row=2, column=1, padx=10, pady=10, columnspan=2)
entrada_octal.bind("<KeyRelease>", convertir_desde_octal)

ttk.Label(root, text="Hexadecimal").grid(row=3, column=0, padx=10, pady=10)
entrada_hexadecimal = ttk.Entry(root, validate="key", validatecommand=vcmd_hexadecimal)
entrada_hexadecimal.grid(row=3, column=1, padx=10, pady=10, columnspan=2)
entrada_hexadecimal.bind("<KeyRelease>", convertir_desde_hexadecimal)

ttk.Button(root, text="1", width=5, command=lambda: insertar_numero("1")).grid(row=4, column=0)
ttk.Button(root, text="2", command=lambda: insertar_numero("2")).grid(row=4, column=1)
ttk.Button(root, text="3", command=lambda: insertar_numero("3")).grid(row=4, column=2)
ttk.Button(root, text="4", command=lambda: insertar_numero("4")).grid(row=5, column=0)
ttk.Button(root, text="5", command=lambda: insertar_numero("5")).grid(row=5, column=1)
ttk.Button(root, text="6", command=lambda: insertar_numero("6")).grid(row=5, column=2)
ttk.Button(root, text="7", command=lambda: insertar_numero("7")).grid(row=6, column=0)
ttk.Button(root, text="8", command=lambda: insertar_numero("8")).grid(row=6, column=1)
ttk.Button(root, text="9", command=lambda: insertar_numero("9")).grid(row=6, column=2)
ttk.Button(root, text="C", command=limpiar_entradas).grid(row=7, column=0)
ttk.Button(root, text="0", command=lambda: insertar_numero("0")).grid(row=7, column=1)

ttk.Button(root, text="A", command=lambda: insertar_numero("A")).grid(row=4, column=3)
ttk.Button(root, text="B", command=lambda: insertar_numero("B")).grid(row=4, column=4)
ttk.Button(root, text="C", command=lambda: insertar_numero("C")).grid(row=4, column=5)
ttk.Button(root, text="D", command=lambda: insertar_numero("D")).grid(row=5, column=3)
ttk.Button(root, text="E", command=lambda: insertar_numero("E")).grid(row=5, column=4)
ttk.Button(root, text="F", command=lambda: insertar_numero("F")).grid(row=5, column=5)

ttk.Button(root, text=chr(9003), command=borrar_ultimo_caracter).grid(row=7, column=2)

ttk.Button(root, text="Escribir binario", command=enfocar_binario).grid(row=0, column=3, padx=10, pady=10, columnspan=3)
ttk.Button(root, text="Escribir octal", command=enfocar_octal).grid(row=1, column=3, padx=10, pady=10, columnspan=3)
ttk.Button(root, text="Escribir decimal", command=enfocar_decimal).grid(row=2, column=3, padx=10, pady=10, columnspan=3)
ttk.Button(root, text="Escribir hexadecimal", command=enfocar_hexadecimal).grid(row=3, column=3, padx=10, pady=10, columnspan=3)

root.mainloop()