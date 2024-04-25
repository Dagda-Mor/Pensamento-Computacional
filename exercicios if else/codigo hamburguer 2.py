Frangolino = 10
Bigtrios = 15
Malvadão = 20

queijo = 2
bacon = 3
ovo = 1

lanche = 0

print('Bem vindo ao Trios Burguer!')
print('qual  hamburgue voce vai esolher?')

carne = input ('escolha Frangolino, Bigtrios, Malvadão:')
if carne == 'Frangolino':
  lanche = lanche + Frangolino

elif carne=='Bigtrios':
  lanche = lanche + Bigtrios

elif carne=='Malvadão':
  lanche = lanche + Malvadão

add_queijo = input('para adicionar queijo digite (s):')
if add_queijo =='s':
  lanche = lanche + queijo

add_bacon = input('para adicionar bacon digite (s):')
if add_bacon =='s':
  lanche = lanche + bacon

add_ovo = input('para adicionar ovo digite (s):')
if add_ovo == "s":
 lanche = lanche + ovo



print (f'o preço do seu hamburguer foi de R${lanche}')