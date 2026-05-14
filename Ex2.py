import multiprocessing
import time
import random

def processamento(id, valores):
    soma: int = 0

    for valor in valores:
        soma = soma + valor
        time.sleep(0.2)

    print("linha", id, "=", soma)

def main():
    id: int = 0
    parametros = []
    vetor = []

    for id in range(3):

        Valor1 = random.randint(1, 100)
        Valor2 = random.randint(1, 100)
        Valor3 = random.randint(1, 100)
        Valor4 = random.randint(1, 100)
        Valor5 = random.randint(1, 100)

        vetor = [Valor1, Valor2, Valor3, Valor4, Valor5]
        
        parametros.append((id, vetor))

    with multiprocessing.Pool(processes=3) as pool:
        pool.starmap(processamento, parametros)

if __name__ == '__main__':
    main()