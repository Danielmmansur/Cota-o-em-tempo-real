import tkinter as tk
import requests

# obter as cotações
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

# Definir cores 
cor_fundo = "#2F4F4F"  # DarkSlateGray
cor_texto = "#F8F8FF"  # Cinza escuro
cor_botao = "#3CB371"  # Verde

# Estilos para os rótulos
estilo_rótulo = {"background": cor_fundo, "fg": cor_texto, "font": ("Arial", 12)}

# Rótulos para as cotações
label_dolar = tk.Label(janela, text="Cotação do Dólar: R$", **estilo_rótulo)
label_euro = tk.Label(janela, text="Cotação do Euro: R$", **estilo_rótulo)
label_bitcoin = tk.Label(janela, text="Cotação do Bitcoin: R$", **estilo_rótulo)

# Botão para atualizar as cotações
estilo_botao = {"background": cor_botao, "fg": "black", "font": ("Arial", 12)}
botao_atualizar = tk.Button(janela, text="Atualizar Cotações", command=obter_cotacoes, **estilo_botao)

# Layout dos elementos
label_dolar.pack(pady=10)
label_euro.pack(pady=10)
label_bitcoin.pack(pady=10)
botao_atualizar.pack(pady=20)

# Primeira atualização das cotações
obter_cotacoes()

# Definir cor de fundo da janela
janela.configure(bg=cor_fundo)

# Iniciar a interface gráfica
janela.mainloop()
