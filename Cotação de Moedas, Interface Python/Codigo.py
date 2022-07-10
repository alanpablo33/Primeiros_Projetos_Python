#a biblioteca Requests (Solicitações) do Python, que permite que você envie solicitações HTTP em Python.
import requests

#Biblioteca para criar interfaces
from tkinter import *

#função que pega a cotação
def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''
    texto_cotacoes["text"] = texto

    #Retiramos o print texto e inserimos o (texto_cotacoes) para chamar a cotação atualizada
    #para sobrescrever a cotação colocamos o ["text"]=texto a variavel já estava criada
    #print(texto)


#pegar_cotacoes()

#iniciando a janela
janela = Tk()
#colocando um titulo na janela
janela.title("Cotação Atual das Moedas")
#geometria da janela
janela.geometry("350x200")

#pedaco de texto
texto_orientacao = Label(janela, text=" Clique no Botão para Ver as Cotação das Moedas Atualizada")
texto_orientacao.grid(column=0, row=0,padx=10 ,pady=10)

#OBS em command ao colocar a função retire o (),
#para que ele execute o comando somente quando o botão for pressionado
botao= Button(janela, text= "BUSCAR COTAÇÕES", command=pegar_cotacoes)
botao.grid(column=0, row= 1,padx=10 ,pady=10)

#vai mostrar a cotação das moedas
texto_cotacoes = Label(janela,text="",)
texto_cotacoes.grid(column=0, row=2,padx=10 ,pady=10)


#comando para manter a janela aberta aguardando as instruções
janela.mainloop()

