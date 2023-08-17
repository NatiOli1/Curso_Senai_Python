aluno = {
    "nome": "Elias",
    "idade": 18,
    "curso": "Administração",
    "disciplina": ["RH", "Excel", "Liderança"]

}

for chave, valor in aluno.items():
    if chave == "disciplinas":
        for disciplina in aluno.get("disciplinas"):
            print(f"Disciplinas {disciplina}")
    else:
        print(f"Chave: {chave}, valor: {valor}")