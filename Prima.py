a = int(input())
if a == 2 or a == 3 or a == 5 or  a == 7:
    print('Angka Prima')
else:
    if a % 2 != 0 and a %3 != 0 and a % 5 != 0 and a % 7 != 0:
        print('Angka Prima')
    else:
        print('Bukan Angka Prima')