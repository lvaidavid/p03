#Írj programot, mely beolvas két egész számot, és kiírja a képernyőre a nagyobbikat!


szam = int(input('Kérlek adj meg egy számot: '))
szam1 = int(input('Kérlek adj meg még egy számot: '))


if szam > szam1:
  print (szam, 'Ez a kisebb')

if szam < szam1:
  print('A két szám között ez a nagyobb->: ',szam1 ) 
