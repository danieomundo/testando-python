import tkinter as tk

janela = tk.TK()

campo_texto = tk.Entry(janela)
botao_enviar = tk.Button(janela, text="Enviar")

campo_texto.pack()
botao_enviar.pack()

janela.mainloop()