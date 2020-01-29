from time import sleep
def terminal_texto():
    arquivo = open('C:/Users/900156/Desktop/Nicole/HbsisAirLines/terminal.txt')
    lista = []
    for linha in arquivo:
        linha = linha.strip()
        lista.append(linha)
    arquivo.close()
    return lista

lista_trip = terminal_texto()

el1=(lista_trip[0])
el2=(lista_trip[1])
el3=(lista_trip[2])
el4=(lista_trip[3])
el5=(lista_trip[4])
el6=(lista_trip[5])
el7=(lista_trip[6])
el8=(lista_trip[7])
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
        embarques(el8,el7)
        aviao.remove(el4)
        carro.append(el4)
        carro.remove(el4)
        terminal.append(el4)
        print(f'O {el4} sai do avião,entra no fortwo e chega no terminal')
        print(f'Estão no avião: {aviao}'),sleep(2)

    elif viagem == 7:
        viagem_fortwo()
        embarques(el1,el4)
        print(f'Estão no avião: {aviao}'),sleep(2)

def salvar_aviao():
    arqui = open('C:/Users/900156/Desktop/Nicole/AirLines/aviao.txt','w')
    dados = '\n'.join(aviao)
    lista_txt = [dados]
    arqui.writelines(lista_txt)
    arqui.close

terminal_texto()

salvar_aviao()