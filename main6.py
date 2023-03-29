preco_unitario = float(input("Digite o preço unitário do produto: "))
quantidade = int(input("Digite a quantidade vendida: "))
desconto = float(input("Digite o percentual de desconto: "))

preco_final = preco_unitario * quantidade * (1 - desconto/100)

print("Preço final com desconto: R$", preco_final)