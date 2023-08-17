def calcula_notas(nota1, nota2, nota3, nota4):
    valor_total = int(nota1) + int(nota2) + int(nota3) + int(nota4)
    return valor_total

def calcula_media_aritmetica(**kwargs):
    calculo_peso1 = int(kwargs.get("peso1")) / 100
    calculo_peso2 = int(kwargs.get("peso2")) / 100
    calculo_peso3 = int(kwargs.get("peso3")) / 100
    calculo_peso4 = int(kwargs.get("peso4")) / 100
    peso = calculo_peso1 + calculo_peso2 + calculo_peso3 + calculo_peso4
    calculo_nota1 = calculo_peso1 * int(kwargs.get("nota1"))
    calculo_nota2 = calculo_peso2 * int(kwargs.get("nota2"))
    calculo_nota3 = calculo_peso3 * int(kwargs.get("nota3"))
    calculo_nota4 = calculo_peso4 * int(kwargs.get("nota4"))
    media_aritmetica = (calculo_nota1 + calculo_nota2 + calculo_nota3 + calculo_nota4) / peso
    return media_aritmetica

def mensagem(total, media_aritmetica):
    print(f"\nO valor total das 4 notas é {total}, e a"
          f"média aritmetica é {media_aritmetica:.2f}")

n1 = input("Nota 1: ")
n2 = input("Nota 2: ")
n3 = input("Nota 3: ")
n4 = input("Nota 4: ")

p1 = input("Peso 1: ")
p2 = input("Peso 2: ")
p3 = input("Peso 3: ")
p4 = input("Peso 4: ")

resultado_media_aritmetica = calcula_media_aritmetica(peso1=p1, peso2=p2, peso3=p3, peso4=p4, nota1=n1, nota2=n2, nota3=n3, nota4=n4)

resultado_notas = calcula_notas(nota1=n1, nota2=n2, nota3=n3, nota4=n4)

mensagem(total=resultado_notas, media_aritmetica=resultado_media_aritmetica)