import tkinter as tk
from tkinter import messagebox
from dicionario import unidades, especiais, dezenas, centenas

def NumeroParaTexto(num):
    if num in centenas:
        return centenas[num]

    partes = []
    centena = (num // 100) * 100
    dezena = (num % 100) // 10 * 10
    unidade = num % 10

    if centena:
        if num == 100:
            partes.append("Cem")
        else:
            partes.append(centenas[centena])

    if dezena + unidade in especiais:
        partes.append(especiais[dezena + unidade])
    else:
        if dezena:
            partes.append(dezenas.get(dezena, ""))
        if unidade:
            partes.append(unidades.get(unidade, ""))

    return " e ".join(filter(None, partes))

def NumeroExtenso():
    try:
        num = int(inputNum.get())
        if num < 0 or num > 9999999:
            messagebox.showerror("Erro", "Digite um número entre 0 e 9.999.999!")
            return

        if num == 0:
            resultado.set("Zero")
            return

        partes = []
        milhao = num // 1_000_000
        milhar = (num % 1_000_000) // 1_000
        centena = (num % 1_000) // 100 * 100
        dezena = (num % 100) // 10 * 10
        unidade = num % 10

        if milhao:
            if milhao == 1:
                partes.append("Um milhão")
            else:
                partes.append(f"{NumeroParaTexto(milhao)} milhões")

        if milhar:
            if milhar == 1:
                partes.append("Mil")
            else:
                partes.append(f"{NumeroParaTexto(milhar)} mil")

        if centena or dezena or unidade:
            partes.append(NumeroParaTexto(num % 1_000))

        resultado.set(" e ".join(partes))
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido!")

# Criando a interface gráfica
janela = tk.Tk()
icon = tk.PhotoImage(file="numeros.png")
janela.iconphoto(True, icon)
janela.title("Número por Extenso")
janela.geometry("400x250")

tk.Label(janela, text="Digite um número até 9.999.999:", font=("Times New Roman", 16)).pack(pady=5)
inputNum = tk.Entry(janela)
inputNum.pack(pady=5)

tk.Button(janela, text="Converter", command=NumeroExtenso).pack(pady=7)

resultado = tk.StringVar()
tk.Label(janela, textvariable=resultado, font=("Times New Roman", 16), wraplength=300).pack(pady=10)

janela.mainloop()
