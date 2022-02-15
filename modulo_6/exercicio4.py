alunos = [
	("Alice", 8),
	("Bob", 7),
  ("Carlos", 9),
]
media = 0
for nome, nota in alunos:
    media = media + nota

print(media/len(alunos))