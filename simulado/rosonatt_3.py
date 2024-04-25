p1 =  int(input("qual é a nota da p1"))
p2 = int(input("qual é a nota da p2"))
media = p1 + p2 / 2
if media >= 7:
  print("aprovado")
elif media < 7:
     print("precisa fazer a p3")
     p3 = int(input("quanto você tioru na p3?"))
     if p3 >= 6:
         print("aprovado")
     else:
         print ("reprovado")