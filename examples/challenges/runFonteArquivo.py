from FonteArquivo import FonteArquivo

fa = FonteArquivo("../../estudantes.csv")

while(fa.possuiDados()):
    print(f"Linha {fa.current +1}: {fa.proximoDado()}")

fa.fecharArquivo()

