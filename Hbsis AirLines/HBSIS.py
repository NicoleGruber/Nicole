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
def estao_aviao():
    sleep(1)
    print(f'Estão no avião: {aviao}')
    sleep(1)
def viagem_fortwo():
    global numero_viagem
    numero_viagem += 1
    print(f'\n========== Viagem {numero_viagem} ==========')
    sleep(1)
    print(f'Estão no terminal: {terminal}')
    sleep(1)
def embarque(mot, pas):
    terminal.remove(pas)
    carro.append(pas)
    print(f'A {mot} e o {pas} embarcaram no Fortwo e vão até o avião')
    sleep(1)
    carro.remove(pas)
    aviao.append(pas)
    print(f'A {pas} desce do Fortwo e embarca no avião ')
def voltar(mot):
    print(f'O {mot} volta no Fortwo para o terminal')
    sleep(1)   
def moto_carro(mot):
    terminal.remove(mot)
    carro.append(mot)
def fica_terminal(mot):
    carro.remove(mot)
    terminal.append(mot)
    print(f'O {mot} desce do Fortwo e fica no terminal')
    sleep(1)
def embarques(mot,pas):
    terminal.remove(mot)
    terminal.remove(pas)
    carro.append(mot)
    carro.append(pas)
    print(f'O {mot} e o {pas} entram no fortwo e vão até o avião')
    sleep(1)
    carro.remove(mot)
    carro.remove(pas)
    aviao.append(mot)
    aviao.append(pas)
    print(f'O {mot} e o {pas} saem do fortwo e entram no avião')
    
for viagem in range(1,8):
    if viagem == 1:
        viagem_fortwo()
        moto_carro(el4)
        embarque(el4, el5)
        estao_aviao()
        voltar(el4)   
    elif viagem == 2:
        terminal.append(el4)
        viagem_fortwo()
        terminal.remove(el4)
        embarque(el4,el6)
        estao_aviao()
        voltar(el4)    
    elif viagem == 3:
        fica_terminal(el4)
        carro.append(el1)
        viagem_fortwo()
        terminal.remove(el1)
        embarque(el1,el2)
        estao_aviao()
        voltar(el1)
    elif viagem == 4:
        terminal.append(el1)
        viagem_fortwo()
        terminal.remove(el1)
        embarque(el1,el3)
        estao_aviao()
        voltar(el1)
    elif viagem == 5:
        terminal.append(el1)
        viagem_fortwo()
        terminal.remove(el1)
        embarque(el1,el4)
        estao_aviao()
        voltar(el1)
    elif viagem == 6:
        fica_terminal(el1)
        viagem_fortwo()
        embarques(el7,el8)
        sleep(1)
        aviao.remove(el4)
        print(f'O {el4} sai do avião e volta com o fortwo para o terminal')
        estao_aviao()
    elif viagem == 7:
        terminal.append(el4)
        viagem_fortwo()
        embarques(el1,el4)
        estao_aviao()