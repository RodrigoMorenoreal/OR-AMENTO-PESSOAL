from tkinter import *
from tkinter import Tk, ttk


#! CORES

co0 = "#2E2D2B"  # Preta
co1 = "#feffff"  # Branca
co2 = "#4fa882"  # Verde
co3 = "#38576b"  # valor
co4 = "#403d3d"  # Letras
co5 = "#e06636"  # - profit
co6 = "#038cfc"  # Azul
co7 = "#3fbfb9"  # Turquesa
co8 = "#26382E"  # + lucro 
co9 = "#005f08"  # + verde lucro
co10 = "#bc2525" # - vermelho despesa
co11 = "#c9c9c9" # Cinza

colors = ['#5588bb', '#66bbbb', '#444466', '#ee9944', '#bb5555']

# Criando a janela
janela = Tk()
janela.title("Sistema de Orçamento Pessoal")
janela.geometry('900x650')
janela.configure(background=co11)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

# Criando Frames
frame_cima = Frame(janela, width=900, height=50, bg=co1, relief="flat")
frame_cima.grid(row=0, column=0)

frame_meio = Frame(janela, width=900, height=361, bg=co1, pady=20, relief="raised")
frame_meio.grid(row=1, column=0, padx=0, pady=1, sticky=NSEW)   

frame_baixo = Frame(janela, width=900, height=300, bg=co1, relief="flat")
frame_baixo.grid(row=2, column=0, padx=10, pady=0, sticky=NSEW)


janela.mainloop()
