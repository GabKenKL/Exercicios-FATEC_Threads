import multiprocessing
import time

def processamento(param):
    time.sleep(0.5)
    print("Thread #", param)

def main():
    id: int = 0
    params: int = [0]*5

    for id in range(5):
        params[id] = id

    with multiprocessing.Pool(processes=5) as pool:
        pool.map(processamento, params)

if __name__ == '__main__':
    main()