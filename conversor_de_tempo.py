def converter_tempo():
    segundos_totais = int(input("Digite a quantidade de segundos: "))

    # Cálculo das horas, minutos e segundos restantes
    horas = segundos_totais // 3600
    resto = segundos_totais % 3600
    minutos = resto // 60
    segundos = resto % 60

    print(f"{segundos_totais} segundos equivalem a: {horas}h {minutos}m {segundos}s")

# Executa a função
converter_tempo()