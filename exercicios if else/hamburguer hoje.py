hhamburgueres = {
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


print("escolha um hamburguer:")
for nome,preço in hhamburgueres.items():
    print(f"{nome} : R${preço}")
    