ativos = []

# Entrada da quantidade de ativos
quantidadeAtivos = int(input())

# Entrada dos códigos dos ativos
for _ in range(quantidadeAtivos):
    codigoAtivo = input()
    ativos.append(codigoAtivo)

# Ordenar os ativos em ordem alfabética
ativos.sort()

# Exibir os ativos em ordem alfabética
for ativo in ativos:
    print(ativo)