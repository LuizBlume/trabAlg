import random
# Gerar gabarito
alternativas = ["A", "B", "C", "D", "E"]
gabarito = []

for i in range(20):
    gabarito.append(random.choice(alternativas))
with open("gabarito.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(", ".join(gabarito))

# Lista de nomes dos candidatos
nomes = [
    "João Silva",
    "Maria Souza",
    "Pedro Santos",
    "Ana Oliveira",
    "Carlos Lima",
    "Fernanda Rocha",
    "Lucas Pereira",
    "Juliana Costa",
    "Marcos Alves",
    "Patricia Mendes",
]

# Gerar candidatos
candidatos = []

for i in range(1, 101):
    nome = random.choice(nomes)
    respostas = []
    
    for j in range(20):
        respostas.append(random.choice(alternativas))

    candidato = [str(i), nome] + respostas
    candidatos.append(candidato)

# Salvar candidatos no arquivo
with open("candidatos.txt", "w", encoding="utf-8") as arquivo:
    for candidato in candidatos:
        linha = ", ".join(candidato)
        arquivo.write(linha + "\n")

# Ler gabarito
with open("gabarito.txt", "r", encoding="utf-8") as arquivo:
    gabarito = arquivo.readline().strip().split(", ")

# Calcular notas dos candidatos
classificacao = []

with open("candidatos.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        dados = linha.strip().split(",")
        id_candidato = dados[0]
        nome = dados[1]
        respostas = dados[2:]
        nota = 0

        for i in range(20):
            if respostas[i] == gabarito[i]:
                nota += 1

        classificacao.append([id_candidato, nome, nota])

# Ordenar classificação pela maior nota
classificacao.sort(key=lambda x: x[2], reverse=True)

# Gerar arquivo de classificação
with open("classificacao.txt", "w", encoding="utf-8") as arquivo:
    for candidato in classificacao:
        linha = candidato[0] + "," + candidato[1] + ", " + str(candidato[2])
        arquivo.write(linha + "\n")

print("Arquivos gerados com sucesso!")
