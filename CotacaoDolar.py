cotacao_dolar = float(input("Digite a cotação do dólar:"))
valor_dolares = float(input("Digite o  valor em dólares:"))

valores_reais = valor_dolares * cotacao_dolar

print(f"O valor equivalente em Reais é: R${valores_reais:.2f}")