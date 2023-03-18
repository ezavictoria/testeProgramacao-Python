import json

#  carrega os dados de faturamento do arquivo JSON
with open('faturamento.json') as f:
    faturamento = json.load(f)

# calcula o menor valor de faturamento
menor_faturamento = min(faturamento)

#  calcula o maior valor de faturamento
maior_faturamento = max(faturamento)

#  calcula a média mensal de faturamento
media_mensal = sum(faturamento) / len(faturamento)

#  calcula o número de dias com faturamento acima da média
dias_acima_media = sum(1 for f in faturamento if f > media_mensal)

print("Menor faturamento:", menor_faturamento)
print("Maior faturamento:", maior_faturamento)
print("Dias acima da média:", dias_acima_media)