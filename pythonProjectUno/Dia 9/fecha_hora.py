import datetime

mi_hora = datetime.time(9, 5)
print(type(mi_hora))
print(mi_hora)
print(mi_hora.hour)
print(mi_hora.minute)

mi_fecha = datetime.date(2025,5,29)
print(mi_fecha)
print(mi_fecha.year)
print(mi_fecha.ctime())
# imprimir fecha de hoy
print(mi_fecha.today())
