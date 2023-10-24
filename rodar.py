import tkinter as tk
import requests

# Função para obter as cotações
def obter_cotacoes():
    cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    cotacoes = cotacoes.json()
    cotacao_dolar = cotacoes['USDBRL']['bid']
    cotacao_euro = cotacoes['EURBRL']['bid']
    cotacao_bitcoin = cotacoes['BTCBRL']['bid']

    label_dolar.config(text=f"Cotação do Dólar: R$ {cotacao_dolar}")
    label_euro.config(text=f"Cotação do Euro: R$ {cotacao_euro}")
    label_bitcoin.config(text=f"Cotação do Bitcoin: R$ {cotacao_bitcoin}")

# Configuração da janela
janela = tk.Tk()
janela.title("Cotações de Moedas")

# Rótulos para as cotações
label_dolar = tk.Label(janela, text="Cotação do Dólar: R$")
label_euro = tk.Label(janela, text="Cotação do Euro: R$")
label_bitcoin = tk.Label(janela, text="Cotação do Bitcoin: R$")

# Botão para atualizar as cotações
botao_atualizar = tk.Button(janela, text="Atualizar Cotações", command=obter_cotacoes)

# Layout dos elementos
label_dolar.pack()
label_euro.pack()
label_bitcoin.pack()
botao_atualizar.pack()

# Primeira atualização das cotações
obter_cotacoes()

# Iniciar a interface gráfica
janela.mainloop()
