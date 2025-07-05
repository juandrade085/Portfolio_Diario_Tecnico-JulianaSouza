import calendar
from datetime import date
mês = int(input("Diga um número referente ao mês do ano\n(Ex. Julho: 7, Junho: 6): "))
ano = date.today().year
print (calendar.month(ano, mês))