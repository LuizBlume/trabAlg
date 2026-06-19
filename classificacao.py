# Ler o gabarito
with open("gabarito.txt", "r", encoding="utf-8") as arquivo:
    gabarito = arquivo.readline().strip().split(",")

# Lista para armazenar os resultados
classificacao = []

# Ler os candidatos
with open("candidatos.txt", "r", encoding="utf-8") as arquivo:

    for linha in arquivo:

        dados = linha.strip().split(",")

        id_candidato = dados[0]
        nome = dados[1]

        # CPF = dados[2]
        # Idade = dados[3]

        respostas = dados[4:]

        nota = 0

        # Compara cada resposta com o gabarito
        for i in range(len(gabarito)):
            if respostas[i] == gabarito[i]:
                nota += 1

        classificacao.append([id_candidato, nome, nota])

# Gerar o arquivo classificacao.txt
with open("classificacao.txt", "w", encoding="utf-8") as arquivo:

    for candidato in classificacao:
        arquivo.write(
            f"{candidato[0]},{candidato[1]},{candidato[2]}\n"
        )

print("Classificacao gerada com sucesso!")