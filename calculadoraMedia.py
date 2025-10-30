def ler_nota(mensagem):
    while True:
        try:
            nota = float(input(mensagem))
            if nota == int(nota):
                print("Digite a nota com casas decimais (ex: 7.5).")
            else:
                return nota
        except ValueError:
            print("Entrada inválida. Digite um número com ponto decimal.")

# Leitura das notas
N1 = ler_nota("Digite a nota 1: ")
N2 = ler_nota("Digite a nota 2: ")
N3 = ler_nota("Digite a nota 3: ")
N4 = ler_nota("Digite a nota 4: ")

# Cálculo da média ponderada
media = (N1 * 2 + N2 * 3 + N3 * 4 + N4 * 1) / 10
print(f"Media: {media:.1f}")

# Verificação da situação do aluno
if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    nota_exame = ler_nota("Digite a nota do exame: ")
    print(f"Nota do exame: {nota_exame:.1f}")
    media_final = (media + nota_exame) / 2
    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {media_final:.1f}")
