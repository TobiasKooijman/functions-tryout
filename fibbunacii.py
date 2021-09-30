vraag = input('Hoeveel nummers wil je? ')

## Valuables


def calcu():
    num = 0
    num1 = 1
    som = 0
    print("")
    print("------------------------")
    print("")
    print(som)
    print(num1)
    for i in range(0,int(vraag)):
        num = num
        num1 = num1
        som = num1+num
        print(som)
        num= num1
        num1 = som
    snede = 'De gulden snede is: '+ str(num1)
    print("")
    print(snede)
    print("")
    print("------------------------")
    print("")
calcu() 