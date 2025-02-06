MAIOR_IDADE = 18
IDADE_ESPECIAL = 12


idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH!")


if idade >= MAIOR_IDADE:
    print("Maior idade, pdoe tirar CNH")
else:
    print("Não pode tirar CNH")


if idade >= MAIOR_IDADE:
    print("mairo de idade, pode tirar CNH")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teoricas, mas não pdoe fazer aulas praticas")
else:
    print("Não pode tirar CNH")