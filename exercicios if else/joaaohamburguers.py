 ##### hamburgues ####
hamburgueres = {
    "frangolino": 10.0,
    "Big Trios": 15.0,
    "Malvadão": 20.0
}

 ##### ingredientes_extras ####

ingredientes_extras = {
    "Oueijo": 1.5,
    "Bacon": 2.0,
    "Ovo": 1.0,
    "Tomate": 0.5,
    "Alface": 0.3
}
##### hamburguers_disponiveis_ ####

print("Escolha o seu hambúrguer:")
for nome, preco in hamburgueres.items():
    print(f"{nome}: R${preco}")

# Solicitando ao usuário que escolha um hambúrguer
escolha = input("Digite o nome do hambúrguer que deseja: ")

###### dizer_se_o _hamburguer_esta_na_lista ####

if escolha in hamburgueres:
    Valor_final = hamburgueres[escolha]
    print(f"Você escolheu o {escolha}.")

    ###### Ingredientes_extras ######

    print("\nIngredientes extras disponíveis:")
    for ingrediente, preco_ingrediente in ingredientes_extras.items():
        print(f"{ingrediente}: R${preco_ingrediente}")

    #### escolheendo_ingredientes_extras ####

    escolha_ingredientes = input("\nDigite os ingredientes extras que deseja separados por vírgula (ou deixe em branco para nenhum): ")
    ingredientes_escolhidos = escolha_ingredientes.split(",")

    # Adicionando o preço dos ingredientes extras ao total
    for ingrediente in ingredientes_escolhidos:
        if ingrediente.strip() in ingredientes_extras:
            Valor_final += ingredientes_extras[ingrediente.strip()]

    #### Valor_total#####
    print(f"\nPreço total: R${Valor_final}")
else:
    print("Hambúrguer não disponível.")
