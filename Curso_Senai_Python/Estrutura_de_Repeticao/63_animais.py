import json

animais = dict[
    {
        "Animal": "Cachorro Pastor",
        "Idade": 3,
        "Fator_idade_humano": 12,
        "Idade_de_humano": 0
    },
    {
        "Animal": "Cachorro Fila",
        "Idade": 4,
        "Fator_idade_humano": 10,
        "Idade_de_humano": 0
    },
    {
        "Animal": "Cachorro Golden",
        "Idade": 2,
        "Fator_idade_humano": 8,
        "Idade_de_humano": 0
    },
    {
        "Animal": "Papagaio",
        "Idade": 8,
        "Fator_idade_humano": 5,
        "Idade_de_humano": 0
    },
    {
        "Animal": "Gato Siamês",
        "Idade": 4,
        "Fator_idade_humano": 7,
        "Idade_de_humano": 0
    },
    {
        "Animal": "Cachorro Husky",
        "Idade": 3,
        "Fator_idade_humano": 9,
        "Idade_de_humano": 0
    },
]

for animal in animais:
    idades_humano = animal.get("Idade") * animal.get("Fator_idade_humano")
    animal.get["Idade_de_humano"] = idades_humano
    eh_cachorro = animal.get("animal").startswith("Cachorro")

    if eh_cachorro and animal.get("Idade_de_humano") >= 30:
        print(f"----Informações do Animal----")
        print(json.dumps(animal, sort_keys=True, indent=4))




