print(5 + 2)   # 7  soma
print(5 - 2)   # 3  subtração
print(5 * 2)   # 10 multiplicação
print(5 / 2)   # 2.5 divisão

print(5 // 2)  # 2  divisão inteira
print(5 % 2)   # 1  módulo (resto)
print(5 ** 2)  # 25 potência
print(2 ** 0.5) # 1.41 raiz quadrada

resultado = 2 + 3 * 4      
resultado2 = (2+3) * 4     
# 14, não 20
# 20

nota1, peso1 = 8.0, 2
nota2, peso2 = 6.0, 3
media = (nota1*peso1 +
nota2*peso2) / (peso1+peso2)
print(f"Média: {media:.2f}")

print(5 == 5)   # True  igual
print(5 != 3)   # True  diferente
print(5 > 3)    
# True  maior
print(5 < 3)    
# False menor
print(5 >= 5)   # True  maior ou igual
print(5 <= 4)   # False menor ou igual

"abc" == "abc"     
"abc" == "ABC"     
# True
# False (case
#sensitive)
"banana" > "abacaxi"  # True (alfabética)

idade = 20
tem_carteira = True

x = 10
x += 5    # x = x + 5   → 15
x -= 3    
# x = x - 3   → 12
x *= 2    # x = x * 2   → 24
x /= 4    # x = x / 4   → 6.0
x //= 2   # x = x // 2  → 3.0
x **= 2   # x = x ** 2  → 9.0
