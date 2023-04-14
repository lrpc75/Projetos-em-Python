import tkinter as tk
from Funcoes import *

root = tk.Tk()
root.geometry('555x307')

# Adicionando o rótulo de seleção
titulo = tk.Label(root, text="Selecione o conteúdo:")
titulo.grid(row=0, column=0)

# Cria a lista selecionável
lista = tk.Listbox(root, selectmode=tk.SINGLE)

# Adiciona itens à lista selecionável
itens = gerarListaLimpa()

for item in itens:
    lista.insert(tk.END, item)
lista.grid(row=1, column=0)

# Adicionando o rótulo de avisos
titulo = tk.Label(root, text="Avisos:")
titulo.grid(row=0, column=1)
#Cria caixa de avisos
caixaDeAvisos = tk.Text(root, width=47, height=13)
caixaDeAvisos.grid(row=1, column=1)


# Adicionando um rótulo de quantidade
titulo = tk.Label(root, text="Digite a quantidade:")
titulo.grid(row=2, column=0, sticky="nswe")
# Adicionando uma caixa de quantidade
entradaQuantidade = tk.Entry(root)
entradaQuantidade.grid(row=3, column=0, sticky="nswe")


# Adicionando um rótulo de quantidade
titulo = tk.Label(root, text="Digite um nome para sua prova:")
titulo.grid(row=2, column=1, sticky="nswe")
# Adicionando uma caixa de nomeação
entradaNome = tk.Entry(root)
entradaNome.grid(row=3, column=1, sticky="nswe")


# Adicionando o botão de Gerar Prova
def gerarProvaPressed():
    conteudo = lista.get(lista.curselection())
    quantidade = int(entradaQuantidade.get())
    filename = conteudo + ".txt"
    nome = "_Prova_Padrao"
    
    aviso = tentarGerarProva(filename, quantidade, nome)
    
    if aviso[0] == "Prova Gerada com Sucesso":
        gerarAviso(aviso[0])
        gerarAviso('Questões usadas:\n')
        
        for questao in aviso[1]:
            questaoUsada = "Questão " + str(questao)
            gerarAviso(questaoUsada)
    else:
        gerarAviso(aviso[0])
    gerarAviso("")
    
gerarProvaButton = tk.Button(root, text="Gerar Prova Padrão", command=gerarProvaPressed)
gerarProvaButton.grid(row=4, column=0, sticky="nswe")

# Adicionando o botão de Excluir Prova
def excluirProvaPressed():
    aviso = excluirProva()
    gerarAviso(aviso)
    
excluirProvaButton = tk.Button(root, text="Excluir Prova Padrão", command=excluirProvaPressed)
excluirProvaButton.grid(row=5, column=0, sticky="nswe")

# Adicionando o botão de Gerar Prova Nomeada
def gerarProvaNomeadaPressed():
    conteudo = lista.get(lista.curselection())
    quantidade = int(entradaQuantidade.get())
    conteudo = conteudo + ".txt"
    nome = entradaNome.get()
    
    aviso = tentarGerarProva(conteudo, quantidade, nome)
    
    if aviso[0] == "Prova Gerada com Sucesso":
        gerarAviso(aviso[0])
        gerarAviso('Questões usadas:\n')
        
        for questao in aviso[1]:
            questaoUsada = "Questão " + str(questao)
            gerarAviso(questaoUsada)
    else:
        gerarAviso(aviso[0])
    gerarAviso("")
    
excluirProvaButton = tk.Button(root, text="Gerar Prova com nome escolhido", command=gerarProvaNomeadaPressed)
excluirProvaButton.grid(row=4, column=1, sticky="nswe")

#Atualiza os avisos vindos de Gera Avisos
def gerarAviso(aviso):
    caixaDeAvisos.insert(tk.END, aviso + "\n")

root.mainloop()
