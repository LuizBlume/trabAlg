import random

alternativas = ["A", "B", "C", "D", "E"]

gabarito = [random.choice(alternativas) for _ in range(20)]

with open("gabarito.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(",".join(gabarito))