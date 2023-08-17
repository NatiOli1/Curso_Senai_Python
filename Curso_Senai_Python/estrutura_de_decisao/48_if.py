nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota:"))

media = (nota1 + nota2) / 2

if media >= 9.8:
    print(f"Está de parabéns, sua média foi {media}")
elif media >= 6.5:
    print(f"Você está de aprovado, sua média foi {media}")
elif media >= 4.8:
    print(f"Você está de recuperação, sua média foi {media}")
else:
    print(f"Você está reprovado, sua média foi {media}")