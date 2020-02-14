
class Person:
    def __init__(self, name):
        self.name = name

    def avanzar(self):
        print('Ando caminando')


class Ciclista(Person):
    def __init__(self, name):
        super().__init__(name)

    def avanzar(self):
        print(f'Ando moviendome en mi bicicleta')


def main():
    persona = Person('David')
    persona.avanzar()

    ciclista = Ciclista('Daniel')
    ciclista.avanzar()


if __name__ == '__main__':
    main()
