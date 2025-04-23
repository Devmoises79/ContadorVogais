frase = input("Digite uma frase: ").lower()
contagem = {"a":0, "e":0, "i":0, "o":0, "u":0}

for letra in frase:
    if letra in contagem:
        contagem[letra] += 1

print("Contagem de vogais:")
for vogal, qtd in contagem.items():
    print(f"{vogal}: {qtd}")