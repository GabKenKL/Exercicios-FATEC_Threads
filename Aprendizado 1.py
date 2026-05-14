#Algoritmo não paralelo

def operacao(param):
    cont: int = 0
    print('Iniciando a operação', param)
    for cont in range (10):
        print('Rodando a operação', param)
    print('Encerrando a operação', param)

def main():
    i: int = 0
    for i in range(3):
        operacao(i)

if __name__ == '__main__':
    main()
