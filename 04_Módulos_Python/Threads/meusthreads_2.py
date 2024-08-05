from time import sleep
from threading import Thread
from threading import Lock

def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)
   
   
# Caso 1 de threads em paralelo 
"""t1 = Thread(target=vai_demorar, args=('Olá mundo 1!', 5))
t1.start()

t2= Thread(target=vai_demorar, args=('Olá mundo 2!', 1))
t2.start()

t3 = Thread(target=vai_demorar, args=('Olá mundo 3!', 7))
t3.start()

for i in range(20):
    print(i)
    sleep(.5)"""


"""# Caso 2 de Threads em paralelo
t1 = Thread(target=vai_demorar, args=('Olá mundo!', 10))
t1.start()
t1.join()

print('Thread acabou!')
"""

# Caso de problemas com Threads
class Ingressos:
    """
    Classe que vende ingressos
    """
    
    def __init__(self, estoque):
        self.estoque = estoque
        # Cadeado para não dessincronizar as threads
        self.lock = Lock()
        
    def comprar(self, quantidade):
        
        # Tranca o método
        self.lock.acquire()
        if self.estoque < quantidade:
            print('Não temos ingressos suficientes')
            # Libera o método na condição 1
            self.lock.release()
            return
        
        sleep(1)
        
        self.estoque -= quantidade
        print(f'Você compro {quantidade} ingressos.'
              f' Ainda temos {self.estoque} em estoque!'
        )
        # Libera o método na condião 2
        self.lock.release()
    
if __name__ == '__main__':
    ingressos = Ingressos(10)
    
    for i in range (1, 10):
        t = Thread(target=ingressos.comprar, args=(i,))
        t.start()        
    print(ingressos.estoque)
