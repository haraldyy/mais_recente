def recente(dia,mes,ano,diad,mesd,anod):
    valorano=dia+mes+ano
    valoranod=diad+mesd+anod
    if valorano > valoranod:
        print(f'{dia}/{mes}/{ano}')
    else:
        print(f'{diad}/{mesd}/{anod}')
def main():
    dia=int(input(''))
    mes=int(input(''))
    ano=int(input(''))
    diad=int(input(''))
    mesd=int(input(''))
    anod=int(input(''))
    recente(dia,mes,ano,diad,mesd,anod)
if __name__=='__main__':
    main()
