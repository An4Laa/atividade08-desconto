valor = float(input("Digite valor em real: "))
desconto = float(input("Digite a porcentagem (%) de desconto: "))
desconto2 = (valor * desconto) / 100
resultado = valor - desconto2
print(f"""Valor do produto: {valor}
    Valor do desconto: {desconto2}
    Produto com desconto: {resultado}""")