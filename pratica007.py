def calcular_troco():
    valor_compra = float(input("Digite o valor da compra: R$ "))
    valor_pago = float(input("Digite o valor pago: R$ "))

    if valor_pago < valor_compra:
        falta = valor_compra - valor_pago
        print(f"Valor insuficiente. Faltam R$ {falta:.2f}.")
    else:
        troco = valor_pago - valor_compra
        print(f"Troco a ser devolvido: R$ {troco:.2f}")

# Executa a função
calcular_troco()
