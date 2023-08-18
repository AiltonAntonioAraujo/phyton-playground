# O aluno so é aprovado se atingir nota 5

nota = int(input("Insira a nota do aluno:"))

if(nota > 5):
    print("Aluno aprovado")
else:
    print("Aluno reprovado")

if(nota % 2 == 0):
    print("A nota "+str(nota)+" é par!")
else:
    print("A nota "+str(nota)+" é impar")