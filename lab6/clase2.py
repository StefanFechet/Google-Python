class Catalog_prajituri:
    cookies_list = []

    def __init__(self, nume, pret, gramaj):
        self.nume = nume
        self.pret = pret
        self.gramaj = gramaj
        Catalog_prajituri.cookies_list.append(self)

    def __repr__(self):
        return repr((self.nume, self.pret, self.gramaj))

    @classmethod
    def print_cookies_gramaj(cls):
        list = sorted(Catalog_prajituri.cookies_list, key=lambda catalog: catalog.gramaj)
        for i in list:
            print('{} - gramaj: {}'.format(i.nume, i.gramaj))

    @classmethod
    def print_cookies_pret(cls):
        list = sorted(Catalog_prajituri.cookies_list, key=lambda catalog: catalog.pret)
        for i in list:
            print('{} - pret: {}'.format(i.nume, i.pret))


class Tort(Catalog_prajituri):
    def setter(self, etajat=False, glazura='ciocolata'):
        self.etajat = etajat
        self.glazura = glazura

    def ret_glazura(self):
        return self.glazura

    def ret_etajat(self):
        return self.etajat


class Fursec(Catalog_prajituri):
    pass


def main():
    tort1 = Tort('Cheesecake', 70, 100)
    tort2 = Tort('Tort diplomat', 100, 50)
    tort3 = Tort('Tort alcazar', 75, 75)

    fursec1 = Fursec('Fursecuri cu ciocolata', 5, 25)
    fursec2 = Fursec('Fursecuri cu unt', 3, 20)
    fursec3 = Fursec('Fursecuri americane', 4, 30)

    Catalog_prajituri.print_cookies_gramaj()
    print('\n')
    Catalog_prajituri.print_cookies_pret()
    print('\n')
    tort2.setter(True, 'cacao')
    print('{} cu glazura de {}'.format(tort2.nume, tort2.ret_glazura()))
    if tort2.ret_etajat():
        print('{} etajat'.format(tort2.nume))
    else:
        print('{} neetajat'.format(tort2.nume))

    print('\n')
    tort3.setter(True, 'zahar ars')
    print('{} cu glazura de {}'.format(tort3.nume, tort3.ret_glazura()))
    if tort3.ret_etajat():
        print('{} etajat'.format(tort3.nume))
    else:
        print('{} neetajat'.format(tort3.nume))


if __name__ == "__main__":
    main()
