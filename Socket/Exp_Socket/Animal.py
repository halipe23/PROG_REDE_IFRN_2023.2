class animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        pass

class Cachorro(animal):
    def fazer_som(self):
        return 'Au au!'

class Gato(animal):
    def fazer_som(self):
        return 'Maiu!'
    
cachorro = Cachorro('Rex')
gato = Gato('Felix')

print(cachorro.nome)
print(cachorro.fazer_som())
print('-'*50)
print(gato.nome)
print(gato.fazer_som())