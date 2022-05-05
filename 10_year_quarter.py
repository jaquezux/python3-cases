month = int(input("Digite um mês entre 1 e 12: "))

def quarter_of(month):
    if month >= 1 and month <= 3:
        return "\nEsse mês faz parte do First Quarter"
    elif month >= 4 and month <= 6:
        return "\nEsse mês faz parte do Second Quarter"
    elif month >= 7 and month <= 9:
        return "\nEsse mês faz parte do Third Quarter"
    else:
        return "\nEsse mês faz parte do Fourth Quarter"

print(quarter_of(month))