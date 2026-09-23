preco_original = float(input("Digite o preço original: R$ "))
desconto_percentual = float(input("Digite a porcentagem de desconto (%): "))

valor_desconto = preco_original * (desconto_percentual / 100)
preco_final = preco_original - valor_desconto

print(f"Preço final com desconto: R$ {preco_final:.2f}")
