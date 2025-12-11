pontuacoes = [5, 9, 3, 10, 2, 7, 8]
criticas_encontradas = 0

for pontos in pontuacoes:
    if pontos >=8:
        criticas_encontradas += 1
print(f"Maquinas em situação criticas = {criticas_encontradas}")