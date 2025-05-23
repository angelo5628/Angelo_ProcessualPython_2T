aniversario = 26
contador = 0

while contador <= 100:
    multiplicando = aniversario * contador
    contador+= 1
    if multiplicando > 1000:
        print(f"O numero {multiplicando} é maior que 1000!")
    print(multiplicando)
