# (Parte 1) Threads - Executando processamentos em paralelo

from time import sleep
from threading import Thread

class MyThread(Thread):
    def __init__(self, texto: str, tempo: int):
        self.texto = texto
        self.tempo = tempo
        
        super().__init__()
        
    def run(self):
        sleep(self.tempo)
        print(self.texto)
            
t1 = MyThread('Thread 1', 3)
t1.start()

t2 = MyThread('Thread 2', 5)
t2.start()

t3 = MyThread('Thread 3', 2)
t3.start()

for i in range(20):
    print(i)
    sleep(1)