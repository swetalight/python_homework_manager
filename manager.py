from datetime import datetime

from contextlib import contextmanager



class MyManager():

    def __init__(self, name_file):
        self.name_file = name_file

    def __enter__(self):

        self.start = datetime.now()
        self.cook_book_rez = self.composition_bluda(self.name_file)
        self.stop = datetime.now()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def composition_bluda(self, name_file):

        composition = list()
        cook_book = {}
        with open(name_file, encoding='utf-8') as f:
            # print(f.read())
            for line in f:
                str = line.rstrip('\n')
                bludo = str.rstrip('\n')
                str = f.readline()
                ll_menu = []
                # print ('bludo',bludo)
                kol_vo = int(str.rstrip('\n'))
                # print('kol-vo',kol_vo)
                for massiv in range(kol_vo):
                    composition = []
                    str = f.readline()
                    str = str.rstrip('\n')
                    for i in str.split(' | '):
                        composition.append(i)
                    ll_menu.append(
                        {'ingridient_name': composition[0], 'quantity': int(composition[1]), 'measure': composition[2]})
                cook_book[bludo] = ll_menu
        print('=============================================')
        print('========cook_book============================')
        print('=============================================')
        print(cook_book)
        print('=============================================')
        return cook_book


if __name__== '__main__':
    with  MyManager('blyda.txt') as mymanager:
        print('Старт программы',str(mymanager.start))
        print('Стоп программы', str(mymanager.stop))
        print('Время выполнения', str(mymanager.stop - mymanager.start))