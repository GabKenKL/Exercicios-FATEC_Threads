#ALGORITMO PARALELO

import multiprocessing #multiprocessamento
import time #vai dar a impressão que as coisas estão ocorrendo uma atrás da outra, mas tudo junto ao mesmo tempo

def operacao(param):
    cont: int = 0
    print('Iniciando a operação', param)
    for cont in range (10):
        print('Rodando a operação', param)
        time.sleep(0.1) #cada vez que rodar a operação, será posto em estado de bloqueado por um tempo determinado
    print('Encerrando a operação', param)

def main():
#   forma de chamada SEQUENCIAL
#   i: int = 0
#   for i in range(3):
#       operacao(i)

#   chamada com paralelismo
    p: int = 0
    num_threads: int = 0
    params: int = [0]*3 #recebe um vetor de parametros, onde cada posição é uma thread. Ex.: Na posição 0, é da 1° thread, a posição 1 é da 2° Thread...

    num_threads = 3

    for p in range(3):
        params[p] = p

    with multiprocessing.Pool(processes=num_threads) as pool:
        pool.map(operacao, params)


if __name__ == '__main__':
    main()
