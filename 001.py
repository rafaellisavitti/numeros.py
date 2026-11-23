lista = [2, 5, 3, 4, 1]
n = len(lista)

for i in range(n):
    for j in range(0, n - i - 1):
        if lista[j] > lista[j + 1]:
            # Troca os elementos de posição
            lista[j], lista[j + 1] = lista[j + 1], lista[j]
            # Mostra cada passo da troca na tela
            print(lista)

numeros = [5, 2, 3]

for i in range(len(numeros) - 1):
    if numeros[i] > numeros[i + 1]:
        numeros[i], numeros[i + 1] = numeros[i + 1], numeros[i]
    print(numeros)

