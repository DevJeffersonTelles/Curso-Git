# Operadores Lógicos
# not, and e or

# not -> True se torna False e False se torna True
v = True
f = False

# print(not v) # False
# print(not f) # True

# print(not 5 > 2) # False
# print(not 2 < 1) # False

# and -> O and só retorno True se ambos os valores forem True
a = 5
b = 10
c = 2
d = 8

# print(a > b and c > d) # False
# print(a > b and c < d) # False
# print(c < d and b < c) # False
# print(a < b and b > c) # True

# or -> So retorna False se ambos os valores forem Falso
print(a > b or b == 11) # False
print(b > a or b == 10) # True

nome = "Jefferson"
idade = 30

print(nome == "João" or idade > 20) # True