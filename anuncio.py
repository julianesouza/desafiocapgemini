'''
    Desenvolvido por: Juliane Rodrigues de Souza

'''
from datetime import datetime

VIEW_POR_REAL = 30
CLIQUE_POR_VIEW = 12
SHARE_POR_CLIQUE = 3

class Anuncio:
    def __init__(self, nome, cliente, data_inicio, data_fim, invest_por_dia):
        self.nome = nome
        self.cliente = cliente
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.invest_por_dia = invest_por_dia
    
class AnuncioRelatorio:
    def __init__(self, valor_total_investido, qtd_max_views, qtd_max_cliques, qtd_max_comps, cliente, tempo_inicio, tempo_fim):
        self.valor_total_investido = valor_total_investido
        self.qtd_max_views = qtd_max_views
        self.qtd_max_cliques = qtd_max_cliques
        self.qtd_max_comps = qtd_max_comps
        self.cliente = cliente
        self.tempo_inicio = tempo_inicio
        self.tempo_fim = tempo_fim

def cadastrar():
    print("\nCadastro\n")
    nome = input("Nome do anuncio: ")
    cliente = input("Cliente: ")
    data_inicio_f = input("Data Inicio [dd/mm/aaaa]: ")
    data_inicio = datetime.strptime(data_inicio_f, "%d/%m/%Y")
    data_fim_f = input("Data Fim [dd/mm/aaaa]: ")
    data_fim = datetime.strptime(data_fim_f, "%d/%m/%Y")
    investimento = float(input("Investimento por dia: "))

    novo_anuncio = Anuncio(nome=nome, cliente=cliente, data_inicio=data_inicio, data_fim=data_fim, invest_por_dia=investimento)

    print("\nCadastro concluido!\n")

    return novo_anuncio

def filtrar_por_cliente(array_anuncios, y, cliente):

    print("\n----------Filtrar por cliente----------\n")
    k = 0
    for x in array_anuncios:
        if(x.cliente == cliente):
            print("Nome do anuncio: " + x.nome + "\n")
            print("Cliente: " + x.cliente + "\n")
            print("Data de inicio: ")
            print(x.data_inicio)
            print("\nData fim: ")
            print(x.data_fim)
            print("\nInvestimento por dia: ")
            print(x.invest_por_dia)
            print("\nValor total investido: ")
            print(y[k].valor_total_investido)
            print("\nMaximo de views: ")
            print(y[k].qtd_max_views)
            print("\nMaximo de cliques: ")
            print(y[k].qtd_max_cliques)
            print("\nMaximo de compartilhamentos: ")
            print(y[k].qtd_max_comps)
            print("\n------------------------------\n")
            k+=1

def filtrar_por_tempo(array_anuncios, y, tempo_inicio, tempo_fim):
    
    print("\n----------Filtrar por intervalo de tempo----------\n")
    k = 0
    for x in array_anuncios:
        
        if(x.data_inicio >= tempo_inicio and x.data_fim <= tempo_fim):
            
            print("Nome do anuncio: " + x.nome + "\n")
            print("Cliente: " + x.cliente + "\n")
            print("Data de inicio: ")
            print(x.data_inicio)
            print("\nData fim: ")
            print(x.data_fim)
            print("\nInvestimento por dia: ")
            print(x.invest_por_dia)
            print("\nValor total investido: ")
            print(y[k].valor_total_investido)
            print("\nMaximo de views: ")
            print(y[k].qtd_max_views)
            print("\nMaximo de cliques: ")
            print(y[k].qtd_max_cliques)
            print("\nMaximo de compartilhamentos: ")
            print(y[k].qtd_max_comps)
            print("\n------------------------------\n")
            k+=1
        
def calculadora(anuncio):
    #faz todos os calculos e retorna um objeto
    dias = dias_total(anuncio.data_inicio, anuncio.data_fim)
    valor_total_investido = dias * anuncio.invest_por_dia
    investimento_inteiro = (int(valor_total_investido)) #parte inteira do investimento total
    views = investimento_inteiro * VIEW_POR_REAL 

    qtd_max_cliques = 0
    qtd_max_comps = 0
    contador = 0

    cliques = (int)(int(views/100) * CLIQUE_POR_VIEW)
    qtd_max_cliques += cliques

    comps = (int)(int(cliques/20) * SHARE_POR_CLIQUE)

    qtd_max_comps += comps

    novas_views = 40 * comps

    views += novas_views

    while contador < 3:
        
        cliques = (int)(int(novas_views/100) * CLIQUE_POR_VIEW)
        qtd_max_cliques += cliques

        comps =(int)(int(cliques/20) * SHARE_POR_CLIQUE)
        qtd_max_comps += comps

        novas_views = 40 * comps
        contador += 1
        views += novas_views

    relatorio = AnuncioRelatorio(valor_total_investido=valor_total_investido, qtd_max_views=views, 
    qtd_max_cliques=qtd_max_cliques,
    qtd_max_comps=qtd_max_comps, 
    cliente=anuncio.cliente, 
    tempo_inicio=anuncio.data_inicio, 
    tempo_fim=anuncio.data_fim)

    return relatorio   

def dias_total(data_inicio, data_fim):
    #calcula o total de dias entre datas
    dias_totais = (data_fim - data_inicio).days

    return dias_totais

def menu():

    AnuncioArray = []
    RelatorioArray = []

    while True:
        print("\nAperte: ")
        print("1 - Para cadastrar novo anuncio")
        print("2 - Para acessar relatorios")
        print("0 - Para encerrar o programa")

        escolha = input("Opcao: ")

        if escolha == '1':

            novo_anuncio = cadastrar()
            relatorio_do_anuncio = calculadora(novo_anuncio)
            AnuncioArray.append(novo_anuncio)
            RelatorioArray.append(relatorio_do_anuncio)

        if escolha == '2':

            print("\nFiltrar\n")
            print("a - Filtrar por intervalo de tempo")
            print("b - Filtrar por cliente\n")

            opcao_de_filtro = input("Opcao: ")

            if (opcao_de_filtro == 'a'):

                data_inicio_f = input("Data Inicio [dd/mm/aaaa]: ")
                tempo_inicio = datetime.strptime(data_inicio_f, "%d/%m/%Y")
                data_fim_f = input("Data Fim [dd/mm/aaaa]: ")
                tempo_termino = datetime.strptime(data_fim_f, "%d/%m/%Y")
                filtrar_por_tempo(AnuncioArray, RelatorioArray, tempo_inicio, tempo_termino)

            if (opcao_de_filtro == 'b'):
                nome_cliente = input("Nome do cliente: ")
                filtrar_por_cliente(AnuncioArray, RelatorioArray, nome_cliente)

            else:
                pass

        if escolha == '0':
            break

menu()