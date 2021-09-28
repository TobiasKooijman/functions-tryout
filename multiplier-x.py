# input

tfl = input('Van welk getal wilt u de tafel zien? ')

def MDTFL():
    for i in range(1,11):
        num = int(tfl) * i
        print(num)

MDTFL()