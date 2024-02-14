
from threading import Thread
from time import sleep

# função
def vai_demorar(texto: str, tempo: int):
    sleep(tempo)
    print(texto)

# OBS: args=(tupla)
t1 = Thread(target=vai_demorar, args=('Thread 1', 5)) # executar em paralelo
t1.start() # iniciar execução

t2 = Thread(target=vai_demorar, args=('Thread 2', 1)) # executar em paralelo
t2.start() # iniciar execução

t3 = Thread(target=vai_demorar, args=('Thread 3', 2)) # executar em paralelo
t3.start() # iniciar execução

for i in range(20):
    print(i)
    sleep(.5)
