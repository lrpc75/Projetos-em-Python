import random
import os

#------------------------------------------------------------INFORMAÇÕES GLOBAIS

questionTam = 7
diretorio_atual = os.getcwd()
diretorio_provas_criadas = os.path.join(diretorio_atual, 'Provas_Criadas')
diretorio_conteudos = os.path.join(diretorio_atual, 'Conteudos')

#---------------------------------------------------------------------INFORMAÇÃO

def whoManyLines(filename):
    with open(filename, "r") as arquivo:
        linhas = 0
        for linha in arquivo:
            linhas += 1
            
    return linhas

def read_specific_line(filename, line_number):
    with open(filename, 'r') as arquivo:
        lines = arquivo.readlines()
        
        return lines[line_number - 1]

def sorteio(filename, quantidade):
    tam = int(whoManyLines(filename)/questionTam)
    x = quantidade
    numeros = random.sample(range(1, tam + 1), x)
    
    return numeros

def listaDeArquivosTxt():
    
    txt_files = []
    inicializarLocais()
    
    for file in os.listdir(diretorio_conteudos):
        if file.endswith(".txt"):
            txt_files.append(file)
    return txt_files

#----------------------------------MANIPULAÇÕES DE ARQUIVO E TRATAMENTO DE TEXTO

def inicializarLocais():

    if not os.path.exists(diretorio_provas_criadas):
        os.makedirs(diretorio_provas_criadas)
        
    if not os.path.exists(diretorio_conteudos):
        os.makedirs(diretorio_conteudos)

def formatarQuestao(contador,questao):
    questao_sem_numero = questao.split(".", 1)[1]
    questaoFormatada = str(contador) + ". " + questao_sem_numero
    return questaoFormatada

def gerarListaLimpa():
    itens_txt = listaDeArquivosTxt()
    itens = set(item.replace('.txt', '') for item in itens_txt)
    itens = sorted(itens)

    return itens

#----------------------------------------------------------DETALHES DAS QUESTÕES

def textoDaQuestao(filename, questao):
    questaoLinha = ((questionTam * (questao - 1)) + 1)
    return read_specific_line(filename, questaoLinha)

def gabaritoDaQuestao(filename, questao):
    questaoLinha = ((questionTam * (questao - 1)) + 2)
    return read_specific_line(filename, questaoLinha)

def alternativa_A_DaQuestao(filename, questao):
    questaoLinha = ((questionTam * (questao - 1)) + 3)
    return read_specific_line(filename, questaoLinha)

def alternativa_B_DaQuestao(filename, questao):
    questaoLinha = ((questionTam * (questao - 1)) + 4)
    return read_specific_line(filename, questaoLinha)

def alternativa_C_DaQuestao(filename, questao):
    questaoLinha = ((questionTam * (questao - 1)) + 5)
    return read_specific_line(filename, questaoLinha)

def alternativa_D_DaQuestao(filename, questao):
    questaoLinha = ((questionTam * (questao - 1)) + 6)
    return read_specific_line(filename, questaoLinha)

#--------------------------------------------------------------------------AÇÕES

def tentarGerarProva(filename, quantidade, nome): #Retorna se foi bem sucedida
    #inicializarLocais()
        
    caminho_da_prova = os.path.join(diretorio_provas_criadas, nome) + ".txt"
    caminho_do_conteudo = os.path.join(diretorio_conteudos, filename)
    
    try:
        with open(caminho_do_conteudo, 'r') as f:
            quantidadeDeQuestoes = int(whoManyLines(caminho_do_conteudo)/questionTam)
            if quantidade > quantidadeDeQuestoes:
                aviso = ("Erro: O conteúdo tem " + str(quantidadeDeQuestoes) + " questões, selecione no máximo esse valor") 
                questoesSorteadas = []
            else:

                limparSaida(caminho_da_prova)
                
                questoesSorteadas = sorteio(caminho_do_conteudo, quantidade)
                contador = 0
                gabarito = []

                descricaoDoArquivo = "Esse arquivo contem " + str(quantidade) + " questões do conteúdo " + filename
                gerarSaida(descricaoDoArquivo, caminho_da_prova)
                gerarSaida("\n\n", caminho_da_prova)
                
                for questao in questoesSorteadas:
                    contador += 1
                    gabarito.append(gabaritoDaQuestao(caminho_do_conteudo, questao))
                    textoDaQuestaoFormatado = formatarQuestao(contador, textoDaQuestao(caminho_do_conteudo, questao))
                    gerarSaida(textoDaQuestaoFormatado, caminho_da_prova)
                    gerarSaida(alternativa_A_DaQuestao(caminho_do_conteudo, questao),caminho_da_prova)
                    gerarSaida(alternativa_B_DaQuestao(caminho_do_conteudo, questao),caminho_da_prova)
                    gerarSaida(alternativa_C_DaQuestao(caminho_do_conteudo, questao),caminho_da_prova)
                    gerarSaida(alternativa_D_DaQuestao(caminho_do_conteudo, questao),caminho_da_prova)
                    gerarSaida("\n", caminho_da_prova)

                gerarGabarito(gabarito, caminho_da_prova, questoesSorteadas)
                
                aviso = "Prova Gerada com Sucesso"

    except FileNotFoundError:
        aviso = "Erro: Conteúdo não encontrado, verifique se o nome do conteúdo foi escrito corretamente, não use acentos nem espaços."
        questoesSorteadas = []
        
    return aviso, questoesSorteadas

def gerarGabarito(gabarito, caminho_da_prova, questoesSorteadas):
    contador = 0
    for i in range(len(gabarito)):
        gabarito[i] = gabarito[i].replace('\n', '')
        gabarito[i] = gabarito[i].split("= ", 1)[1]
    
    gabaInicio = ">-------------GABARITO-------------<"
    gerarSaida(gabaInicio, caminho_da_prova, )
    for resposta in gabarito:
        contador += 1
        
        if contador < 10 :
            if questoesSorteadas[contador - 1] < 10:
                gabaFormatado = ("| Questão " + str(contador) + "  | "+ resposta + " |" + " Lista = " + str(questoesSorteadas[contador - 1]) + "  |")
            else:
                gabaFormatado = ("| Questão " + str(contador) + "  | "+ resposta + " |" + " Lista = " + str(questoesSorteadas[contador - 1]) + " |")

        else:
            if questoesSorteadas[contador - 1] < 10:
                gabaFormatado = ("| Questão " + str(contador) + " | " + resposta + " |" + " Lista = " + str(questoesSorteadas[contador - 1]) + "  |")
            else:
                gabaFormatado = ("| Questão " + str(contador) + " | " + resposta + " |" + " Lista = " + str(questoesSorteadas[contador - 1]) + " |")
        gerarSaida("\n", caminho_da_prova)
        gerarSaida(gabaFormatado, caminho_da_prova)
                    
    gerarSaida("\n", caminho_da_prova)
    gabaFim = "<---------------------------------->"
    gerarSaida(gabaFim, caminho_da_prova)

def limparSaida(caminho_da_prova):
    with open(caminho_da_prova, 'w') as f:
        pass

def gerarSaida(informação, arquivoDeSaida):
    with open(arquivoDeSaida, 'a') as f:
        f.write(informação)

def excluirProva():
    #inicializarLocais()
    caminho_da_padrao = os.path.join(diretorio_provas_criadas, "_Prova_Padrao") + ".txt"
    if os.path.exists(caminho_da_padrao):
        os.remove(caminho_da_padrao)
        return "Prova excluída com sucesso!"
    else:
        return "A Prova já foi excluída."
