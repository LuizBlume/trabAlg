import random

alternativas = ["A", "B", "C", "D", "E"]

nomes = [
    "João Silva", "Maria Souza", "Pedro Santos", "Ana Oliveira",
    "Carlos Lima", "Juliana Costa", "Lucas Pereira", "Fernanda Rocha"
]

# Gerar gabarito
gabarito = [random.choice(alternativas) for _ in range(20)]

with open("gabarito.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(",".join(gabarito))

# Matriz de candidatos
candidatos = []

for i in range(1, 101):

    nome = random.choice(nomes)

    cpf = (
        f"{random.randint(100,999)}."
        f"{random.randint(100,999)}."
        f"{random.randint(100,999)}-"
        f"{random.randint(10,99)}"
    )

    idade = random.randint(18, 60)

    respostas = [random.choice(alternativas) for _ in range(20)]

    candidato = [i, nome, cpf, idade] + respostas

    candidatos.append(candidato)

# Salvar candidatos
with open("candidatos.txt", "w", encoding="utf-8") as arquivo:
    for candidato in candidatos:
        arquivo.write(",".join(map(str, candidato)) + "\n")

# Calcular notas
classificacao = []

for candidato in candidatos:

    id_candidato = candidato[0]
    nome = candidato[1]

    respostas = candidato[4:]

    nota = 0

    for i in range(len(gabarito)):
        if respostas[i] == gabarito[i]:
            nota += 1

    classificacao.append([id_candidato, nome, nota])

# Gerar classificação
with open("classificacao.txt", "w", encoding="utf-8") as arquivo:
    for candidato in classificacao:
        arquivo.write(
            f"{candidato[0]},{candidato[1]},{candidato[2]}\n"
        )

print("Arquivos gerados com sucesso!")