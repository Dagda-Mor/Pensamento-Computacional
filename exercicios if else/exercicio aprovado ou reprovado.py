def verificar_aprovacao(nota_p1, nota_p2):
    media = (nota_p1 + nota_p2) / 2
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

def main():
    nota_p1 = float(input("Digite a nota da P1: "))
    nota_p2 = float(input("Digite a nota da P2: "))

    resultado = verificar_aprovacao(nota_p1, nota_p2)
    print(f"O aluno está {resultado}.")

if __name__ == "__main__":
    main()
