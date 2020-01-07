from time import sleep
el1='Piloto'
el2='Oficial 1'
el3='Oficial 2'
el4='chefe de serviço de voo'
el5='comissária 1'
el6='comissária 2'
el7='Bandido'
el8='Policial'
carro = []
aviao = []
terminal = [el1,el2,el3,el4,el5,el6,el7,el8]
numero_viagem=0
    
def viagem_fortwo():
    global numero_viagem
    numero_viagem += 1
    print(f'\n========== Viagem {numero_viagem} =========='),sleep(2)
    print(f'Estão no terminal: {terminal}'),sleep(2)
    

def embarque(mot, pas):
    terminal.remove(mot)
    terminal.remove(pas)    
    carro.append(mot)
    carro.append(pas)
    print(f'A {mot} e o {pas} embarcaram no Fortwo e vão até o avião'),sleep(2)
    print(f'A {pas} desce do Fortwo e embarca no avião '),sleep(2)
    carro.remove(pas)
    aviao.append(pas)
    print(f'O {mot} volta no Fortwo para o terminal'),sleep(2)
    terminal.append(mot)   

def embarques(mot,pas):
    terminal.remove(mot)
    terminal.remove(pas)
    carro.append(mot)
    carro.append(pas)
    print(f'O {mot} e o {pas} entram no fortwo e vão até o avião'),sleep(2)
    carro.remove(mot)
    carro.remove(pas)
    aviao.append(mot)
    aviao.append(pas)
    print(f'O {mot} e o {pas} saem do fortwo e entram no avião'),sleep(2)
    
for viagem in range(1,8):
    if viagem == 1:
        viagem_fortwo()
        embarque(el4, el5)
        print(f'Estão no avião: {aviao}'),sleep(2)

    elif viagem == 2:
        viagem_fortwo()
        embarque(el4,el6)
        print(f'Estão no avião: {aviao}'),sleep(2)

    elif viagem == 3:
        viagem_fortwo()
        embarque(el1,el2)
        print(f'Estão no avião: {aviao}'),sleep(2)

    elif viagem == 4:
        viagem_fortwo()
        embarque(el1,el3)
        print(f'Estão no avião: {aviao}'),sleep(2)

    elif viagem == 5:
        viagem_fortwo()
        embarque(el1,el4)
        print(f'Estão no avião: {aviao}'),sleep(2)

    elif viagem == 6:
        viagem_fortwo()
        embarque(el8,el1)
        print(f'Estão no avião: {aviao}'),sleep(2)

    elif viagem == 7:
        viagem_fortwo()
        embarques(el7,el8)
        print(f'Estão no avião: {aviao}'),sleep(2)