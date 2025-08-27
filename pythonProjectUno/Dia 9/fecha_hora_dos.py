from datetime import datetime
from datetime import date

mi_fecha = datetime(2025, 5, 15, 22, 10, 15, 2500)

mi_fecha = mi_fecha.replace(month=11)

print(mi_fecha)

nacimiento = date(1995,3,5)
defuncion = date(2095,5,20)

vida = defuncion - nacimiento
print("vivio ", vida)

despierta = datetime(2025,5,28,7,10)
durmio = datetime(2025,5,28,23,00)

vigilia = durmio - despierta
print(vigilia)