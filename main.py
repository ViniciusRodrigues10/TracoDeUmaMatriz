ordemMatriz = int(input())

matriz = []
for i in range(ordemMatriz):
    valores = str(input()).split(" ")
    matriz.append(valores)

soma = 0
concatResposta = ""
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if i == j:
            matriz[i][j] = float(matriz[i][j])
            valorDiagonalPrincipal = "{:.2f}".format(matriz[i][j])
            if i != (len(matriz) - 1):
                concatResposta += "(" + str(valorDiagonalPrincipal) + ") " + "+ "
            else:
                concatResposta += "(" + str(valorDiagonalPrincipal) + ")"
            soma += matriz[i][j]

print(f"tr(A) = {concatResposta} = {soma:,.2f}")