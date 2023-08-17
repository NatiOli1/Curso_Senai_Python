dias = input("digite os dias: ")
horas = input("digite as horas: ")
minutos = input("digite os minutos: ")
segundos = input("digite os segundos: ")

dias_segundos = int(dias) * 86400
horas_segundos = int(horas) * 3600
minutos_segundos = int(minutos) * 60

total_segundos = dias_segundos + horas_segundos + minutos_segundos + int(segundos)

print(f"Dias: {dias}\n Horas: {horas}\n Minutos: {minutos}\n Segundos: {segundos}\n Convertido em segundos: {total_segundos}")

