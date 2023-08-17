def calcula_tempo(**kwargs):
    dias_segundos = int(kwargs.get("Dias")) * 86400
    horas_segundos = int(kwargs.get("Horas")) * 3600
    minutos_segundos = int(kwargs.get("Minutos")) * 60
    total_segundos = dias_segundos + horas_segundos + minutos_segundos + int(kwargs.get("Segundos"))
    return total_segundos


def mensagem(Dias, Horas, Minutos, Segundos, Convertido):
    print(f"Dias: {Dias}\nHoras: {Horas}\nMinutos: {Minutos}\nSegundos: {Segundos}\n"
          f"Convertido em segundos: {Convertido:.2f}")


dias = input("digite os dias: ")
horas = input("digite as horas: ")
minutos = input("digite os minutos: ")
segundos = input("digite os segundos: ")

resultado_segundos = calcula_tempo(Dias=dias, Horas=horas, Minutos=minutos, Segundos=segundos)

mensagem(Dias=dias, Horas=horas, Minutos=minutos, Segundos=segundos, Convertido=resultado_segundos)
