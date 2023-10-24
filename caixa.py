import tkinter as tk

# Função para atualizar as cotações
def atualizar_cotacoes():
    # Substitua as chamadas de API pelas suas próprias chamadas para obter os valores reais
    valor_dolar = "5.20"  # Substitua pelo valor atual do dólar
    valor_euro = "6.10"   # Substitua pelo valor atual do euro
    valor_bitcoin = "60,000"  # Substitua pelo valor atual do Bitcoin

    label_dolar.config(text=f"Cotação do Dólar: R$ {valor_dolar}")
    label_euro.config(text=f"Cotação do Euro: R$ {valor_euro}")
    label_bitcoin.config(text=f"Preço do Bitcoin: $ {valor_bitcoin}")

# Configuração da janela
janela = tk.Tk()
janela.title("Cotações de Moedas")

# Rótulos para as cotações
label_dolar = tk.Label(janela, text="Cotação do Dólar: R$")
label_euro = tk.Label(janela, text="Cotação do Euro: R$")
label_bitcoin = tk.Label(janela, text="Preço do Bitcoin: $")

# Botão para atualizar as cotações
botao_atualizar = tk.Button(janela, text="Atualizar Cotações", command=atualizar_cotacoes)

# Layout dos elementos
label_dolar.pack()
label_euro.pack()
label_bitcoin.pack()
botao_atualizar.pack()

# Primeira atualização das cotações
atualizar_cotacoes()

# Iniciar a interface gráfica
janela.mainloop()