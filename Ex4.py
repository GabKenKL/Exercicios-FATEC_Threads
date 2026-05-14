import multiprocessing
import platform
import subprocess

def processamento(param):
    vetor_processo: str = []
    linha: str = ''
    saida: str = ''
    thread: str = ''
    vetor_linha: str = ''


        #DEFININDO A THREAD
    if param == 'ping -4 -n 10 www.uol.com.br' or param == 'ping -4 -c 10 www.uol.com.br':
        thread = 'Uol'

    elif param == 'ping -4 -n 10 www.terra.com.br' or param == 'ping -4 -c 10 www.terra.com.br':
        thread = 'Terra'

    elif param == 'ping -4 -n 10 www.google.com.br' or param == 'ping -4 -c 10 www.google.com.br':
        thread = 'Google'
        

    vetor_processo = param.split(" ")
    linha = ''
    saida = subprocess.Popen(vetor_processo, stdout=subprocess.PIPE)
    linha = saida.stdout.readline().decode('utf-8', errors = 'ignore')
    while linha != '':
        linha = saida.stdout.readline().decode('utf-8', errors = 'ignore')

        if ('Mdia' in linha):
            print (linha)
            vetor_linha = linha.split(' ')
            print(thread, "=", vetor_linha[12])

        if ('avg' in linha and '/' in linha):
            print (linha)
            vetor_linha = linha.split(' ')
            print(thread, "=", vetor_linha[6])

def main():
    n: int = 0
    vetor_ping: str = ''

    system = platform.system()

    if system == 'Windows':
        ping1 = 'ping -4 -n 10 www.uol.com.br'
        ping2 = 'ping -4 -n 10 www.terra.com.br'
        ping3 = 'ping -4 -n 10 www.google.com.br'

    elif system == 'Linux':
        ping1 = 'ping -4 -c 10 www.uol.com.br'
        ping2 = 'ping -4 -c 10 www.terra.com.br'
        ping3 = 'ping -4 -c 10 www.google.com.br'

    vetor_ping = [ping1, ping2, ping3]

    with multiprocessing.Pool(processes=5) as pool:
        pool.map(processamento, vetor_ping)

if __name__ == '__main__':
    main()