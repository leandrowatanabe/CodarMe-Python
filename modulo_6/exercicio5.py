# Alunos e suas notas representados através de dicionários
alunos = [
	{
		"nome": "Alice",
		"nota": 8,
	},
	{
		"nome": "Bob",
		"nota": 7,
	},
	{
		"nome": "Carlos",
		"nota": 9,
	}
]

media = 0
for aluno in alunos:
    media = media + (aluno['nota'])

print(media/len(alunos))