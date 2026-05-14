import multiprocessing
import random
import time

distancia_maxima: int = 0

def proc(Num, distancia):

    soma = 0

    while soma < distancia:
        salto = random.randint(1, 10)
        soma = soma + salto
        time.sleep(0.2)

        print ("O sapo número", Num, "pulou", salto, "cm!")
    
    print("O sapo número", Num, "chegou!")
    

def main():
    global distancia_maxima
    distancia_maxima = int(input("Digite a distância máxima da corrida: "))
    num: int = 0
    salto: int = 0
    parametros = []

    for num in range(5):
        parametros.append((num, distancia_maxima))

    with multiprocessing.Pool(processes=5) as pool:
        pool.starmap(proc, parametros)

if __name__ == '__main__':
    main()