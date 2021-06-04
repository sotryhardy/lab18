import linecache

def funk(wiersz, plik = 'pantadeusz.txt'):
    if linecache.getline(plik, wiersz) != '':
        print(f'Wiersz {wiersz}: ' + linecache.getline(plik, wiersz).strip('\n'))
    else:
        print(f'Wiersz {wiersz} jest pusty')

funk(8)
funk(12)
funk(60)
funk(98)
funk(104)

print(f'Ilość wierszy: {len(open("pantadeusz.txt", "r").readlines())}')
