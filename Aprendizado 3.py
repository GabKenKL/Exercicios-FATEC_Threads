#ALGORITMO PARALELO

import multiprocessing #multiprocessamento
import time #vai dar a impressão que as coisas estão ocorrendo uma atrás da outra.

def operacao(param, valor):
    cont: int = 0
    res: int = 0
    print('Iniciando a operação', param)
    for cont in range (10):
        print('Rodando a operação', param)
        res = valor ** cont
        print (res)
        time.sleep(0.1) #cada vez que rodar a operação, será posto em estado de bloqueado por um tempo determinado
    print('Encerrando a operação', param)

def main():
#   forma de chamada SEQUENCIAL
#   i: int = 0
#   for i in range(3):
#       operacao(i)

#   chamada com paralelismo
    p: int = 0
    num_thread: int = 0
    params = [(0, 0)]*3 #recebe um vetor de parametros, onde cada posição é uma thread. Ex.: Na posição 0, é da 1° thread, a posição 1 é da 2° Thread...

    num_threads = 3

    for p in range(3):
        params[p] = (p, p + 2)  # "(p,)" É para o parametro, o numero do thread. "(, p + 2)" é o número do valor que será eleveado

    with multiprocessing.Pool(processes=num_threads) as pool:
        pool.starmap(operacao, params)


if __name__ == '__main__':
    main()
