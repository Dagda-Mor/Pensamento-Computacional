##Crie um programa que:
##Dado um inteiro, realize as seguintes ações condicionais:
##Se  for ímpar, imprima Estranho
#Se  for par e estiver no intervalo inclusivo de 2 a 5, imprima Não Estranho
##Se  for par e estiver no intervalo inclusivo de 6 a 20, imprima Estranho
##Se  for par e maior que 20, imprima Não Estranho


number = int(input("digite um numero"))
if number % 2 != 0:
    print("estranho")
elif 2 <= number <= 5:
    print("não estranho")
elif 6 <=number <=30:
    print("estranho")
else:
    print("não estranho")    