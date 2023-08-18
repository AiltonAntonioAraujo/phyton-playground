idade = int(input("Digite a idade:"))
peso = int(input("Digite seu peso:"))
sono = int(input("Digite quantas horas vc dormiu:"))

if (idade > 16) and (idade < 69) and (peso > 50) and (sono >= 6):
    print("Você pode doar sangue!")
else:
    print("Você não pode doar sangue!")


