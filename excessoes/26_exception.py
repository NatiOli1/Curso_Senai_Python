def somar(n1, n2):
    resutado = n1+n2
    return resutado

try:
    numero1 = 10
    numero2 = "b"
    somar(numero1 + numero2)
except Exception as ex:
    print(f"Ocorreu um erro, tente novamente mais tarde{ex}")