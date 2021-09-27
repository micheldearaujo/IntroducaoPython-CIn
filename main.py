"""
Banco de dados para armazenamento e cadastro e restaurantes

@author micheldearaujo
created at  Sep 24 2021 11:19
"""

import ast
import matplotlib.pyplot as plt
import numpy as np

# Configurando constantes
arquivo = "./restaurantes.txt"

restaurantes = {
    123: {
        "cnpj": '123',
        "nome": "faca",
        "avaliacao": 5,
        "qtdeAvaliacoes": 1000,
        "cidade": "recife",
        "localizacao": [1, 0],
        "cozinhas": ["chinesa", "italiana", "hamburguer"]
        },
    126: {
        "cnpj": '126',
        "nome": "faasda",
        "avaliacao": 5,
        "qtdeAvaliacoes": 1000,
        "cidade": "lasanha",
        "localizacao": [1, 0],
        "cozinhas": ["chinesa", "italiana", "hamburguer"]
        }    
}


def menu():
    opcao = int(input("""
    Bem vindo ao sistema de cadastro de restaurantes. O que deseja fazer agora?
    0 - Sair do sistema;
    1 - Mostar este menu de opções;
    2 - Listar todos os restaurantes do banco de dados;
    3 - Adicionar um novo restaurante ao banco de dados;
    4 - Buscar informações de um restaurante no banco de dados;
    5 - Atualizar dados;
    6 - Deletar dados do banco;
    7 - Mostrar o Dashboard do banco de dados;

    Digite apenas o número correspondente à sua ação.
    """))

    if opcao == 0:
        print("Finalizando o programa, volte sempre!")

    elif opcao == 1:
        menu()

    elif opcao == 2:
        listarRestaurantes()

    elif opcao == 3:
        addRestaurant()

    elif opcao == 4:
        buscarRestaurante()

    elif opcao == 5:
        atualizarRestaurante()

    elif opcao == 6:
        deletarRestaurante()

    elif opcao == 7:
        dashBoard()

    else:
        print("Opcão inválida, tente novamente. ")
        menu()

def salvarArquivo(dicionario, nomeArquivo):
    """
    Função que salva um objeto do tipo dicionário em um arquivo txt
    :param dicionario: um objeto do tipo dicionário,
    no qual cada chave é um cnpj e cada valor é um dicionário de Dados
    de um restaurante
    :param nomeArquivo: caminho e nome do arquivo .txt para salvar
    """
    arquivo = open(nomeArquivo, "w")

    for key, value in dicionario.items():
        arquivo.write(str(key) + ";" + str(value) + "\n")
    
def lerArquivo(arquivo):
    """
    Função que abre um arquivo .txt que possui dados dos restaurantes em formato parecido
    com dicionário e transforma as strings em elementos de um dicionário
    :param arquivo: caminho e nome do arquivo.txt a ser lido
    :return: um objeto do tipo dicionário com dados de restaurantes
    """

    restaurantes  = {}
    arquivo = open(arquivo, "r")
    linhas = arquivo.readlines()
    linhasLimpo = [linha.strip("\n") for linha in linhas]
    
    # Transformando os elementos da lista em um dicionário
    # Separando a chave dos valores através do separador "-"
    # So que o valor é um próprio dicionário, e precisamos lê-lo de tal forma
    # Para que o programa funcione corretamente

    for registro in linhasLimpo:
        # Aqui cada linha será separada na string '-', que foi definida a mão para facilitar o armazenamento e leitura
        # do dicionário em arquivo de texto padrão.
        cnpj = registro.split(";")[0]
        dados = registro.split(";")[1]

        # Função externa que transforma uma string de dicionário em um dicionário
        subDic = ast.literal_eval(dados)
        # Adiciona o cnpj do restaurante como key e as suas informações como value
        restaurantes[cnpj] = subDic
    
    return restaurantes

def addRestaurant():
    """
    Função que adiciona novos registros (restaurantes) ao banco de dados (a um dicionário).
    :param arquivo: caminho e nome do arquivo.txt a ser lido
    """
    restaurantes = lerArquivo(arquivo)

    print("Seção de registro de restaurantes. Preencha os campos abaixo para adicionar um novo restaurante ao banco de dados.")
    qtdeAdd = int(input("Quantos registros deseja fazer? "))

    for index in range(qtdeAdd):
        cnpj = input("Digite o CNPJ. ")
        nome = input("Digite o nome do restaurante. ")
        avaliacao = float(input("Digite a avaliação geral do restaurante. "))
        qtdeAvaliacoes = int(input("Digite a quantidade de avaliações que o restaurante possui. "))
        cidade = input("Qual a cidade do restaurante? ")
        loc = input("Quais as coordenadas do restaurante? ").split(',')
        localizacao = [float(l) for l in loc]
        cozinhas = input("Quais tipos de comida o restaurante oferece? (separados por vírgula) ").split(",")

        # Adicionando o novo conjunto de valores em forma de dicionário para
        # O referido cnpj
        restaurantes[cnpj] = {
            "cnpj": cnpj,
            "nome": nome,
            "avaliacao": avaliacao,
            "qtdeAvaliacoes": qtdeAvaliacoes,
            "cidade": cidade,
            "localizacao": localizacao,
            "cozinhas": cozinhas
        }

    print(f"Restaurante {nome} adicionado com sucesso!")

    # Salvando as alterações e voltado ao menu principal
    salvarArquivo(restaurantes, arquivo)
    voltarMenu()

def buscarRestaurante():
    """
    Função que busca restaurantes baseado no CNPJ (id) ou em atributos
    """
    # Criando um dicionário vazio que armazena o resultado da busca
    resultadoPesquisa = {}

    # Lendo o banco de dados 
    restaurantes = lerArquivo(arquivo)

    tipoBusca = input("""
    Bem vindo ao sistema de busca do Banco de Dados de Restaurantes. A partir de que informação desea realizar sua pesquisa?
    cnpj;
    nome;
    avaliacao;
    quantidade de avaliacoes;
    cidade;
    cozinhas;
    (Digite alguma das opções acima)
    """)

    # Cada tipo de elemento terá um tratamento diferente
    if tipoBusca.lower() == 'cnpj':

        cnpj = input(f"Digite o CNPJ do restaurante que deseja encontrar. ")

         # Verificando se o cnpj está no banco de dados
        if cnpj in restaurantes:

            print("-"*40)
            print("O restaurante encontrado foi: \n")
            for key, value in restaurantes[cnpj].items():
                print(key, ":", value)
            return restaurantes[cnpj]

        else:
            print("Nenhum restaurante encontrado. ")

            voltarMenu()
    
    elif tipoBusca in ['nome', 'avaliacao', 'quantidade de avaliacoes', 'cidade', 'coordenadas', 'cozinhas']:
        atributo = input("Digite o termo que deseja pesquisar. ")

        if tipoBusca == 'cozinhas':
            atributo = atributo.split(',')
        elif tipoBusca == 'avaliacao' or tipoBusca == 'quantidade de avaliacoes':
            atributo = float(atributo)

        # Varrendo o dicionário e os subdicionários para encontrar os Restaurantes
        # que dão match com o termo da pesquisa
        for key, value in restaurantes.items():

            # Nested Dict
            for subKey, subValue in value.items():

                # Quando a Key do dicionário interno da match com o tipoBusca, ele verifica se o value 'interno' é igual
                # ao 'atributo', que foi dado pelo usuário
                if (tipoBusca == subKey) and (subValue == atributo):
                    resultadoPesquisa[key] = value

        # Printando o resultado da pesquisa (Pode ter digo encontrado multiplos restaurantes)
        print("\n","-"*10,"Resultado da pesquisa", "-"*10, "\n")
        for key, value in resultadoPesquisa.items():
            print("-"*30)
            for subKey, subValue in value.items():
                print(subKey, ":", subValue)

    else:
        print("** Opção inválida, tente novamente. ")
        buscarRestaurante()

def atualizarRestaurante():
    """
    Função que busca por um restaurante, baseado no CNPJ (id)
    e atualiza qualquer atributo desejado
    """
    restaurantes = lerArquivo(arquivo)

    cnpj = input("Digite o CNPJ do restaurante que deseja atualizar.")
    
    # Verifica se o cnpj existe
    if cnpj in restaurantes:
        print("Você escolheu alterar o restaurante: ")
        for key, value in restaurantes[cnpj].items():
            print(key, ":", value)
        atributo = input("Qual atributo deseja atualizar? ")

        # Verifica se o atributo existe
        if atributo in restaurantes[cnpj]:
            novoAtributo = input("Digite o novo valor para o atributo.")

            # Se o atributo for uma lista, vamos transformar a entrada em uma lista, baseado na vírgula
            if atributo == 'localizacao':
                # Se for localização, transforma uma lista de floats
                novoAtributo = novoAtributo.split(',')
                novoAtributo = [float(atr) for atr in novoAtributo]
                restaurantes[cnpj][atributo] = novoAtributo
            
            # Se for cozinha, transforma em uma lista de strings
            elif atributo == 'cozinhas':
                novoAtributo = novoAtributo.split(',')
                novoAtributo = [item.strip() for item in novoAtributo]
                restaurantes[cnpj][atributo] = novoAtributo
            # Ou transforma em floats
            elif atributo in ['avaliacao', 'qtdeAvaliacoes']:
                novoAtributo = float(novoAtributo)
                restaurantes[cnpj][atributo] = novoAtributo
            
            # Caso contrário, é apenas uma string
            else:
                restaurantes[cnpj][atributo] = novoAtributo

        else:
            print("Atributo invalido. Tente novamente. ")

    else:
        print("Nenhum CNPJ no sistema, verifique e tente novamente.")

    print("\nAtributo atualizado com sucesso!")
    print("Os novos dados do restaurante são:\n")
    for key, value in restaurantes[cnpj].items():
            print(key, ":", value)

    salvarArquivo(restaurantes, arquivo)
    voltarMenu()

def listarRestaurantes():
    """
    Função que lista todos os restaurantes do banco de Dados
    """

    print("\n","*"*40)
    print("Banco de dados de restaurantes")
    restaurantes = lerArquivo(arquivo)
    print(f"No momento existem {len(restaurantes)} restaurantes no banco de dados. \n")

    for key, value in restaurantes.items():
        print("-"*30)
        for subKey, subValue in value.items():
            print(subKey, ":", subValue)

    voltarMenu()

def deletarRestaurante():
    """
    Função que deleta restaurantes baseado em qualquer atributo dos dados.
    """

    # Lendo o dicionário
    restaurantes = lerArquivo(arquivo)

    # Criando um dicionário vazio para armazenar os restaurantes que não
    # Fazem parte do critério de deleção
    novoRestaurantes = {}
    
    print("Bem vindo a seção de eliminação de restaurantes. Antes de realizar qualquer ação, pense bem no que irá fazer.")

    atributo = input("Baseado em qual atributo deseja fazer a deleção? ")
    valorAtributo = input("Digite o valor do atributo. ")

    print(f"Deletando todos os restaurantes cujo {atributo} é {valorAtributo}...")

    # Verificando o tipo do atributo para transformar o input
    if atributo in ['avaliacao', 'qtdeAvaliacoes']:
        atributo = int(atributo)
    elif atributo in ['localizacao', 'cozinhas']:
        atributo = atributo.split(',')
    
    # Itera através do dicionário e subdicionários
    # Para cada chave e valor, verifica se o input é igual
    # ao valor, e se for igual, ele não adiciona no dicionário novo
    for key, value in restaurantes.items():
        for subKey, subValue in value.items():
            if subKey == atributo:
                if subValue != valorAtributo:
                    novoRestaurantes[key] = value

    # Atualizando os dados e voltando ao menu principal
    salvarArquivo(novoRestaurantes, arquivo)

    voltarMenu()

def voltarMenu():
    """
    Função que retorna ao menu principal após ter executado qualquer operação
    """

    opcao = input("\nDeseja voltar ao menu principal (sim ou nao)? ")

    if opcao.lower() == 'sim':
        menu()

    elif opcao.lower() == 'nao':
        print("\n", "-"*40)
        print("Finalizando o programa, volte sempre!")

    else:
        print("Opção invalida. Voltando ao menu.")
        menu()

def dashBoard():
    """
    Função que gera um dashboard com 4 gráficos diferentes
    mostrando informações relevantes do banco de Dados
    """
    # Lendo o dicionário
    restaurantes = lerArquivo(arquivo)

    # Criando um canvas 2x2 e configurando as margens
    fig, axs = plt.subplots(2,2)
    fig.set_constrained_layout_pads(hspace=0.195, wspace=0.038)
    

    def reunirDados():
        """ 
        Função que reune os dados do dicionário e transforma em listas,
        para melhor trabalhar na hora de construir os gráficos
        """

        # Inicializando listas para armazenar os valores do dicionário
        # de forma otimizada para plotagem
        variaveis = []
        nomes = []
        valores = []
        avaliacoes = []
        qtdeAvaliacoes = []
        cidades = []
        cozinhas = []

        # Varrendo o dicionário para pegar chaves e valores
        for key, value in restaurantes.items():
            variaveis.append(list(value.keys()))
            valores.append(list(value.values()))
        variaveis = variaveis[1]

        # Descomprimindo os valores e colocando nas devidas listas
        for lista in valores:
            nomes.append(lista[1])
            avaliacoes.append(lista[2])
            qtdeAvaliacoes.append(lista[3])
            cidades.append(lista[4])
            cozinhas.append(lista[6])

        # Alterando a configuração da lista "cozinhas", que é uma lista
        # de listas, e agora vai ser apenas uma lista
        cozinhasTratado = []
        for item in cozinhas:
            for item2 in item:
                cozinhasTratado.append(item2)

        return nomes, avaliacoes, qtdeAvaliacoes, cidades, cozinhasTratado

    def histogramaAvaliacoes():
        """
        Função que gera um histograma das avaliações dos restaurantes
        """
        
        axs[0,0].hist(avaliacoes)

        #plt.hist(avaliacoes)
        axs[0,0].set_title("Distribuição das avaliações")
        axs[0,0].set_xlabel("Avaliações")
        axs[0,0].set_ylabel("Frequência")

    def barPlotCozinhas():
        """
        Função que gera um gráfico de barras horizontal,
        mostrando a popularidade de cada tipo de cozinha registrada"""
        # Contando os valores de ocorrência das cozinhas
        frequencias = []

        # Criando uma variável tipo "set", para armezenar valores únicos
        comidas = set(cozinhas)

        # Varrendo as ocorrencias das cozinhas e contando os valores
        for comida in comidas:
            frequencias.append(cozinhas.count(comida))
        
        # Transformando o set de volta numa lista
        comidas = list(comidas)
        print(comidas)

        # Plotando os tipos de comidas
        bubble_sizes = [size*400 for size in frequencias]
        #plt.scatter(x=range(len(comidas)),
        #y=frequencias,
        #s=bubble_sizes,
        #alpha = 0.5)

        #fig = plt.figure(figsize=(12,8))
        axs[1,0].barh(comidas, frequencias,
        color='orange')
        axs[1,0].set_title("Comidas mais populares nos restaurantes")
        axs[1,0].set_xlabel("Frequência")

    def bubblePlotQtdeAvaliacoes(qtdeAvaliacoes):
        """
        Função que plota um gráfico de bolhas,
        mostrando a quantidade de avaliações que cada restaurante possui
        """
        # Criando variáveis 'dummy' apenas para posicionar as bolhas
        x = [2, 5, 5, 2.5, 7, 6, 8]
        y = [2, 5, 3, 7.5, 1, 8, 6]
        # Definindo offsets para colocar o texto ao lado de cada bolha
        offsets = [0.6, 1.5, 0.25, 1.0, 0.4, 0.5, 0.5]

        # Plotando o scatter, onde o tamanho dos markers é
        # a quantidade de avaliações
        axs[0,1].scatter(x, y,
        s=qtdeAvaliacoes,
        alpha=0.9)

        # Configurando os textos e eixos
        axs[0,1].set_title("Quantidade de avaliações por restaurante")
        for i, text in enumerate(qtdeAvaliacoes):
            axs[0,1].annotate(text, (x[i]+offsets[i], y[i]))
        for j, text in enumerate(nomes):
            axs[0,1].annotate(text, (x[j]+offsets[j], y[j]-0.5))
        axs[0,1].axis('off')
        axs[0,1].set_xlim(0,11)
        axs[0,1].set_ylim(0, 9)
        #plt.show()

    def pizzaCidades(cidades):
        """
        Função que gera um gráfico de pizzas que mostra
        a quantidade de restaurantes registrados por cidade
        """

        # Contando a ocorrência de cada cidade
        cidadesUnico = set(cidades)
        frequencias = []
        for city in cidadesUnico:
            frequencias.append(cidades.count(city))

        cidadesUnico = list(cidadesUnico)

        # Plotando a pizza

        axs[1,1].pie(frequencias, labels=cidadesUnico,
        autopct='%1.1f%%')
        axs[1,1].set_title("Quantidade de restaurantes por cidade")
        #plt.show()

     # Executando as funções, quando a função mãe for chamada.
    nomes, avaliacoes, qtdeAvaliacoes, cidades, cozinhas = reunirDados()

    histogramaAvaliacoes()
    barPlotCozinhas()
    bubblePlotQtdeAvaliacoes(qtdeAvaliacoes)
    pizzaCidades(cidades)
    #plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    menu()
