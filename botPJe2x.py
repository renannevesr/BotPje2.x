from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import lercsv1
import csv
# abre o arquivo para escrita
file = open('Verif_PJE2X.csv', 'w', newline='', encoding='utf-8')
url = 'https://pje1g.trf5.jus.br/pjeconsulta/ConsultaPublica/listView.seam '
# colocando o webdriver para abrir
browser = webdriver.Chrome(ChromeDriverManager().install())
# mandando a url para webdriver
browser.get(url)
time.sleep(5)
idx = 1
# obtendo o numero de linhas do csv.
num_lines = sum(1 for line in open('nomes.csv'))
# print(num_lines)
while (idx < num_lines):
    # ler a linha(idx) do csv
    cpfO = lercsv1.nomes1[idx]
    lines_cpf = len(cpfO)
    if lines_cpf == 10:
        cpfCorrigido = ['0', cpfO[0], cpfO[1], cpfO[9], cpfO[2],
                        cpfO[3], cpfO[4], cpfO[8], cpfO[5], cpfO[6], cpfO[7]]
    else:
        cpfCorrigido = [cpfO[0], cpfO[1], cpfO[2], cpfO[10], cpfO[3],
                        cpfO[4], cpfO[5], cpfO[9], cpfO[6], cpfO[7], cpfO[8]]
    idx += 1
    # encontrando os paramentros e clicando (selenium)
    PesquisaCPF = browser.find_element_by_xpath(
        '//*[@id="fPP:dpDec:documentoParte"]').send_keys(cpfCorrigido)
    # consultando o CPF.
    PesquisaConfirma = browser.find_element_by_xpath(
        '//*[@id="fPP:searchProcessos"]')
    PesquisaConfirma.click()
    time.sleep(3)
    #urlAtual = browser.current_url
    # criando variavel para gravar no csv
    dadosCompletos1 = ''
    # abrindo a função  do csv para escrever
    Escrever = csv.writer(file, delimiter=',')
    CpfN = cpfO
    try:
        ProcSelenium = browser.find_element_by_xpath(
            '//html/body/div[6]/div/div/div/div[2]/form/div[2]/div/table/tbody/tr/td[2]/a/b')
        ProcessoN = ProcSelenium.text
        # locarlizar a segunda ocorrencia do '-'
        search = ('-')
        buscaPN1 = ProcessoN.find(search)
        buscaPN = ProcessoN.find(search, buscaPN1+1)
        ProcessoBusc = ProcessoN[6:buscaPN]
    except:
        ProcessoBusc = 'Não achou processo no PJE 2.X'
        # transformando tudo em uma matriz
    dados2X = [CpfN, ProcessoBusc]
    time.sleep(2)
    # criando variavel para gravar no csv
    dadosCompletos = ''
    # abrindo a função  do csv para escrever
    Escrever = csv.writer(file, delimiter=',')
    # loop para implementar na variavel.
    for idados in dados2X:
        dadosCompletos += idados + ';'
        # escrita no csv.
    Escrever.writerow([dadosCompletos])
    # limpando o campo da pesquisa
    time.sleep(2)
    limparNome = browser.find_element_by_xpath(
        '//*[@id="fPP:dpDec:documentoParte"]').send_keys(Keys.CONTROL, 'a')
    apagarNome = browser.find_element_by_xpath(
        '//*[@id="fPP:dpDec:documentoParte"]').send_keys(Keys.BACKSPACE)
    time.sleep(2)
