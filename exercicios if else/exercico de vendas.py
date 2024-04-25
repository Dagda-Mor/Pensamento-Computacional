def calcular_bonus(vendas, salario_base):
    if vendas >= 200:
        return salario_base * 0.4
    elif 100 <= vendas <= 200:
        return salario_base * 0.1
    else:
        return 0

def main():
    vendas_vendedor1 = float(input("Digite o número de vendas do vendedor 1: "))
    vendas_vendedor2 = float(input("Digite o número de vendas do vendedor 2: "))
    vendas_vendedor3 = float(input("Digite o número de vendas do vendedor 3: "))

    salario_base_vendedor1 = 700
    salario_base_vendedor2 = 1200
    salario_base_vendedor3 = 2000

    bonus_vendedor1 = calcular_bonus(vendas_vendedor1, salario_base_vendedor1)
    bonus_vendedor2 = calcular_bonus(vendas_vendedor2, salario_base_vendedor2)
    bonus_vendedor3 = calcular_bonus(vendas_vendedor3, salario_base_vendedor3)

    print(f"O bônus do vendedor 1 é: R${bonus_vendedor1}")
    print(f"O bônus do vendedor 2 é: R${bonus_vendedor2}")
    print(f"O bônus do vendedor 3 é: R${bonus_vendedor3}")

if __name__ == "__main__":
    main()
