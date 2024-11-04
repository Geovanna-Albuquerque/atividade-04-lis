#Ler um vetor com 20 idades e exibir a maior e menor.

idades = []

# Ler 20 idades do usuário
for i in range(20):
    idade = int(input(f"Digite a idade {i + 1}: "))
    idades.append(idade)

# Encontrar a maior e a menor idade
maior_idade = max(idades)
menor_idade = min(idades)
print(f"A maior idade é: {maior_idade}")
print(f"A menor idade é: {menor_idade}")

