import calendar

print("ME DIGA SEU ANIVERSÁRIO")
dia_destaque = int(input("DIA: "))
mes = int(input("MÊS: "))
ano = int(input("ANO: "))

calendar.setfirstweekday(calendar.SUNDAY) #Calendário começa no sábado
calendario = calendar.monthcalendar(ano, mes) #Estrutura do mês

nome_mes = calendar.month_name[mes].capitalize()

#Título do calendário centralizado (34 espaços = 7 colunas x 4 + 6 espaços)
print(f"{nome_mes} {ano}".center(34))

#Título dos dias da semana
dias_semana = ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sáb"]
print(" ".join(f"{d:>4}" for d in dias_semana))

for semana in calendario:
    nova_semana = []
    for dia in semana:
        if dia == dia_destaque:
            nova_semana.append(f"\033[0;31m{dia:>4}\033[m")  # dia do aniversário em vermelho
        elif dia == 0:
            nova_semana.append("    ")  # espaço para dias vazios
        else:
            nova_semana.append(f"{dia:>4}")
    print(" ".join(nova_semana))
