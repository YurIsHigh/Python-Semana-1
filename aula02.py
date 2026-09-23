if True:
	print("Bloco indentado")

print("Ainda dentro do if")

print("Fora do if")

nome = "Ana"
sauda = "Olá " + nome
print(sauda)
print("Oi! " * 3)

idade = 25
nome = "Carlos"
print(f"{nome},\n{idade} anos")

preço = 19.999
f"R$ {preço:.2f}"
pct = 0.4567
f"{pct:.1%}"

p = "Python"
p[0] = "J"
# TypeError!
nova = "J"+p[1:]

t = "  Top  "
t.strip()
t.upper()
t.lower()
t.replace(
"a","b")

frase = "Python é uma linguagem"
frase.split()
frase.count("i")
frase.find(
"lingua")
"-".join(
["a","b"])
