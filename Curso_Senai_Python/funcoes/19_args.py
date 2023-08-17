def imprimir_cidade_bairros(cidade, *args):
    print(f"A cidade {cidade} tem os seguintes bairros: ")

    for bairro in args:
        print(bairro)


imprimir_cidade_bairros("Piracicaba", "Centro", "Vila Fátima", "Cecap", "Mário Dedini")