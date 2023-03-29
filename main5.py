# Recebe a área total da casa do usuário
area_total = float(input("Digite a área total da casa (em m²): "))

# Calcula a quantidade de argamassa e rejunte necessários
argamassa = area_total * 2 # 2 kg de argamassa por m² de piso
rejunte = area_total * 0.5 # 0,5 kg de rejunte por m² de piso

# Exibe os resultados para o usuário
print("Para trocar o piso da casa de", area_total, "m² serão necessários:")
print(argamassa, "kg de argamassa")
print(rejunte, "kg de rejunte")