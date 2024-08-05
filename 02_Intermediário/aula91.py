'''
Introdução às Generator Functions em Python
generator = (n for n in range(10000))
'''

def generator(n=0, maximum=0):
    while True:
        yield n
        n += 1

        if n >= maximum:
            return
        
gen = generator(maximum=10000)
for n in gen:
    print(n)