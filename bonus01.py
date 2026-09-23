def converter_segundos():
    segundos_totais = int(input("Digite a quantidade de segundos: "))

    # Constantes de tempo
    SEGUNDOS_POR_MINUTO = 60
    SEGUNDOS_POR_HORA = 3600
    SEGUNDOS_POR_DIA = 86400

    # Cálculos das unidades de tempo
    dias = segundos_totais // SEGUNDOS_POR_DIA
    resto_dias = segundos_totais % SEGUNDOS_POR_DIA

    horas = resto_dias // SEGUNDOS_POR_HORA
    resto_horas = resto_dias % SEGUNDOS_POR_HORA

    minutos = resto_horas // SEGUNDOS_POR_MINUTO
    segundos_restantes = resto_horas % SEGUNDOS_POR_MINUTO

    print(f"\nResultados para {segundos_totais} segundos:")
    print(f"-> {dias} dia(s), {horas} hora(s), {minutos} minuto(s) e {segundos_restantes} segundo(s).")


# Execução da função
converter_segundos()