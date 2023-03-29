# Recebe o valor da duplicata e a quantidade de dias de atraso do usuário
valor_duplicata = float(input("Digite o valor da duplicata: R$"))
dias_atraso = int(input("Digite a quantidade de dias de atraso: "))

# Calcula o valor da multa a ser aplicada
multa = valor_duplicata * 0.05 * dias_atraso

# Calcula o valor final da duplicata com a multa aplicada
valor_final = valor_duplicata + multa

# Exibe o valor final da duplicata para o usuário
print("O valor final da duplicata é R$",valor_final)
