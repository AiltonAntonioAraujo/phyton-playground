from FonteArquivo import FonteArquivo

# Abrir o arquivo especificado
fa = FonteArquivo("../../estudantes.csv")

# Ler e imprimir na tela as linhas do arquivo aberto
while(fa.possuiDados()):
    print(f"Linha {fa.current +1}: {fa.proximoDado()}")

# Encerrar a leitura do arquivo
fa.fecharArquivo()


