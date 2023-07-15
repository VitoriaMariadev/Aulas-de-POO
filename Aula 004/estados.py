class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} já está filmando.')
            return

        print(f'{self.nome} está filmando...')
        self.filmando = True

    def fotografar(self):
        if self.filmando:
           print(f'{self.nome} já está filmando.')
           return
        print(f'{self.nome} está fotografando...')

c1 = Camera('canon')
c1.filmar()
c1.filmar()
print(c1.filmando)