# Escreva um programa para calcular a redução do tempo de vida de um fumante.
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele fumou.
# Considere que um fumante perde 10 minutos de vida a cada cigarro,
# calcule quantos dias de vida um fumante perderá. Exiba o total em dias.

cigarros_por_dia = int(input("Quantidade de cigarros fumados por dia: "))
anos_fumados = int(input("Quantos anos você fumou: "))

total_cigarros = cigarros_por_dia * 365 * anos_fumados
total_minutos_perdidos = total_cigarros * 10
total_dias_perdidos = total_minutos_perdidos // (60 * 24)

print(f"Um fumante perderá aproximadamente {total_dias_perdidos} dias de vida")