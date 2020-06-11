class Catalog:
    def __init__(self, nume, prenume):
        self.nume = nume
        self.prenume = prenume
        self.materii = {}
        self.absente = 0

    def __str__(self):
        if self.absente != 1 and self.absente < 20:
            return 'elevul are {self.absente} absente'.format(self=self)
        if self.absente == 1:
            return 'elevul are o absenta'
        return 'elevul are {self.absente} de absente'.format(self=self)

    def elev_absent(self):
        self.absente += 1

    def motiveaza_absente(self, nr):
        if isinstance(nr, int):
            self.absente -= nr
        elif nr.isdigit():
            self.absente -= int(nr)
        else:
            print('scutirea nu este valida')
        if self.absente < 0:
            self.absente = 0


class Materii(Catalog):
    def adauga_materii(self, materie_noua, lista_note):
        self.materii[materie_noua] = lista_note

    def afiseaza_materii(self):
        lista_materii = ""
        for i in self.materii:
            lista_materii += i + " "
        print("Studentul {} {} are urmatoarele materii: {}".format(self.nume, self.prenume, lista_materii))

    def medie(self):
        for i in self.materii:
            count = 0
            suma_note = 0
            for j in range (0, len(self.materii[i])):
                if isinstance(self.materii[i][j], float) or isinstance(self.materii[i][j], int):
                    count += 1
                    suma_note += self.materii[i][j]
                elif self.materii[i][j].isdigit():
                    count += 1
                    suma_note += int(self.materii[i][j])
                else:
                    try:
                        nota = float(self.materii[i][j])
                        count += 1
                        suma_note += nota
                    except:
                        continue
            print("Medie {} - {}".format(i, suma_note/count))


def main():
    x = Catalog('Ion', 'Roata')

    for i in range(0, 3):
        x.elev_absent()
    x.motiveaza_absente('2')
    print(x.__str__())

    y = Catalog('George', 'Cerc')
    for i in range(0, 4):
        y.elev_absent()
    y.motiveaza_absente(2)
    print(y.__str__())

    m1 = Materii('Ion', 'Roata')
    m2 = Materii('George', 'Cerc')

    m1.adauga_materii('Python', [5, 7, 9])
    m1.adauga_materii('Romana', [10, 8, 9])
    m2.adauga_materii('Python', [6, '7.5', '8'])
    m2.adauga_materii('Matematica', [10, '10.0', '8'])
    m1.afiseaza_materii()
    m1.medie()
    m2.afiseaza_materii()
    m2.medie()
    #m.adauga_materii('Python', [8, 8.5, 10])


if __name__ == "__main__":
    main()
