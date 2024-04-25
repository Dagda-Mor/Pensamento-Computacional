salario  =  2700
vendas =  int(input("numero de vendas é"))
if vendas >=100 and vendas <=300:
    bonus  =  salario * 1.10
    print("o salario é", bonus)
if vendas > 300:
    bonus =  salario * 1.15
    print("o salario é", bonus)
if vendas < 100:
    print ("seu slario não mudou")

